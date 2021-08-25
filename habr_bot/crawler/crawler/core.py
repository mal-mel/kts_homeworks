from bs4 import BeautifulSoup

import asyncio
import logging

from typing import Optional

from .handlers import PageHandler, UrlHandler
from .driver import WebDriver
from .types import Article
from .services import ElasticInterface


class Crawler:
    def __init__(self, base_url: str,
                 workers_num: int,
                 timeout: int,
                 elastic_interface: ElasticInterface):
        self.base_url = base_url
        self.workers_num = workers_num
        self.elastic_interface = elastic_interface

        self._url_handler = UrlHandler(base_url)
        self._page_handler = PageHandler(self._url_handler)
        self._driver = WebDriver(timeout)

        self._urls_queue = asyncio.Queue()
        self._es_worker_queue = asyncio.Queue()
        self._urls_worker_queue = asyncio.Queue()
        self._articles_worker_queue = asyncio.Queue()

        self._already_parsed = set()
        self._already_putted = set()
        self._workers = []

    async def start(self):
        await self._urls_queue.put(self.base_url)
        await self._driver.init(self.workers_num)

        self._init_crawl_workers()
        self._init_es_worker()
        self._init_articles_worker()
        self._init_urls_worker()

        await asyncio.gather(*self._workers)

        await self._urls_queue.join()
        await self._es_worker_queue.join()
        await self._urls_worker_queue.join()
        await self._articles_worker_queue.join()

    def _init_crawl_workers(self):
        for _ in range(self.workers_num):
            t = asyncio.create_task(self._crawl_worker())
            self._workers.append(t)

    def _init_es_worker(self):
        t = asyncio.create_task(self._es_worker())
        self._workers.append(t)

    def _init_articles_worker(self):
        t = asyncio.create_task(self._articles_worker())
        self._workers.append(t)

    def _init_urls_worker(self):
        t = asyncio.create_task(self._urls_worker())
        self._workers.append(t)

    async def _articles_worker(self):
        while True:
            soup, url = await self._articles_worker_queue.get()
            article: Optional[Article] = self._page_handler.get_article_data(soup, url)
            if article:
                logging.info(f"[articles_worker] put '{article.url}' into queue")
                await self._es_worker_queue.put(article)

    async def _urls_worker(self):
        while True:
            soup = await self._urls_worker_queue.get()
            urls = self._page_handler.get_page_urls(soup)
            for url in urls:
                if url not in self._already_parsed and url not in self._already_putted:
                    self._already_putted.add(url)
                    logging.info(f"[urls_worker] put {url} into queue")
                    await self._urls_queue.put(url)

    async def _es_worker(self):
        while True:
            article: Article = await self._es_worker_queue.get()
            if not await self.elastic_interface.is_article_exists(article):
                logging.info(f"[es_worker] insert '{article.url}' into es")
                await self.elastic_interface.insert_article(article)

    async def _crawl_worker(self):
        while True:
            url = await self._urls_queue.get()
            if url not in self._already_parsed:
                self._already_parsed.add(url)
                logging.info(f"[crawl_worker] parse {url}")
                if res := await self._driver.get_html(url):
                    url, html = res
                    self._already_parsed.add(url)
                    soup = BeautifulSoup(html, "lxml")
                    if self._url_handler.is_article_url(url):
                        await self._articles_worker_queue.put((soup, url))
                    await self._urls_worker_queue.put(soup)

    async def stop(self):
        await self._driver.stop()
