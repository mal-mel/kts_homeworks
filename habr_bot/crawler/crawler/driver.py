from pyppeteer import launch
from pyppeteer.launcher import Browser
from pyppeteer.page import Page
from pyppeteer.errors import PyppeteerError
from pyppeteer.network_manager import Request

from typing import Optional

import asyncio


class WebDriver:
    def __init__(self, timeout: int):
        self.timeout = timeout * 1000

        self._pages_queue = asyncio.Queue()
        self._browser: Optional[Browser] = None

    async def init(self, workers_num: int):
        self._browser = await launch()
        for _ in range(workers_num):
            await self._pages_queue.put(await self._create_page())

    async def get_html(self, url: str) -> Optional[tuple]:
        res = None
        page = await self._pages_queue.get()
        try:
            response = await page.goto(url)
            if response and response.ok:
                res = response.url, await response.text()
        finally:
            await self._pages_queue.put(page)
            return res

    async def stop(self):
        while not self._pages_queue.empty():
            page = await self._pages_queue.get()
            await page.close()
        await self._browser.close()

    async def _create_page(self) -> Page:

        async def on_req(req: Request):
            if req.resourceType in ["image", "font", "stylesheet"]:
                await req.abort()
            else:
                await req.continue_()

        page = await self._browser.newPage()
        page.setDefaultNavigationTimeout(self.timeout)
        # await page.setRequestInterception(True)
        # page.on("request", on_req)

        return page
