import aiohttp
import asyncio

from config import LIMIT_REQUEST


async def get_html(session: aiohttp.ClientSession, url: str) -> tuple:
    async with session.get(url) as response:
        html = await response.text()
        return url, html


async def habr_crawler(urls: set):
    connector = aiohttp.TCPConnector(limit_per_host=LIMIT_REQUEST)
    session = aiohttp.ClientSession(connector=connector)
    urls_data = await asyncio.gather(*[get_html(session, url) for url in urls])
    await session.close()
    return urls_data
