import aiohttp
import asyncio


async def get_html(session: aiohttp.ClientSession, url: str) -> str:
    async with session.get(url) as response:
        return await response.text()


async def habr_crawler(urls: list) -> list:
    session = aiohttp.ClientSession()
    urls_contents = await asyncio.gather(*[get_html(session, url) for url in urls])
    await session.close()
    return [
        (urls[i], urls_contents[i]) for i in range(len(urls))
    ]
