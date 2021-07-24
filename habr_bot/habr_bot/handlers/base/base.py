from aiogram import Bot, types

from crawler import habr_crawler

from utils.convert import bytes_to_string, string_to_json
from utils.content_handler import is_html_contains_tags

from . import templates


async def start_handler(message: types.Message):
    await message.reply(templates.HELP_MESSAGE)


async def file_handler(message: types.Message):
    bot_obj = Bot.get_current()

    data = await bot_obj.download_file_by_id(message.document.file_id)
    content = bytes_to_string(data)

    if json_data := string_to_json(content):
        links, tags = json_data["links"], json_data["tags"]
        links_data = await habr_crawler(urls=links)
        if links_data:
            result_links = []
            for url, html in links_data:
                if is_html_contains_tags(html, tags):
                    result_links.append(url)
            if result_links:
                result_links = "\n".join(result_links)
                await message.reply(templates.RESULT.format(links=result_links))
            else:
                tags = ", ".join(tags)
                await message.reply(templates.NOT_FOUND.format(tags=tags))
        else:
            await message.reply(templates.SOMETHING_PROBLEMS)
    else:
        await message.reply(templates.MALFORMED_FILE)
