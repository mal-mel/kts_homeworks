HELP_MESSAGE = """
Привет, этот бот умеет находить статьи на твоем любимом Хабре по заданным ключевым словам.
Отправь мне файл и я пришлю тебе ссылки на статьи :)
"""

RESULT = """
Я нашел следующие статьи:
{links}
"""

NOT_FOUND = """
Я не смог ничего найти по заданным ключевым словам [{tags}] :(
"""

SOMETHING_PROBLEMS = """
Кажется у нас какие-то проблемы... или у Хабра
"""

MALFORMED_FILE = """
Что-то мне не нравится твой файл.
Формат, который я понимаю:
{
    "links": [...],
    "tags": [...]
}
"""
