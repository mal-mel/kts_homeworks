from aiohttp import web


def setup_urls(app: web.Application):
    from server.apps.admin_user.urls import setup_urls
    setup_urls(app)

    from server.apps.bot_user.urls import setup_urls
    setup_urls(app)
