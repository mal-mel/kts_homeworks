from aiogram import types

from crawler import habr_crawler

from utils.convert import bytes_to_string, string_to_json
from utils.content import is_html_contains_tags
from utils.validators import validate_json
from utils.tg_api import get_file_data

from . import templates


async def start_handler(message: types.Message):
    await message.reply(templates.HELP_MESSAGE)


async def file_handler(message: types.Message):
    data = await get_file_data(message.document.file_id)
    content = bytes_to_string(data)
    if validate_json(json_data := string_to_json(content)):
        links, tags = set(json_data["links"]), set(json_data["tags"])
        if links_data := await habr_crawler(urls=links):
            result_links = []
            for url, html in links_data:
                if is_html_contains_tags(html, tags):
                    result_links.append(url)
            tags = ", ".join(tags)
            if result_links:
                result_links = "\n".join(result_links)
                await message.reply(templates.RESULT.format(links=result_links, tags=tags))
            else:
                await message.reply(templates.NOT_FOUND.format(tags=tags))
        else:
            await message.reply(templates.SOMETHING_PROBLEMS)
    else:
        await message.reply(templates.MALFORMED_FILE, parse_mode="Markdown")
