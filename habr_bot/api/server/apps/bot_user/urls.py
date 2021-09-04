from aiohttp import web

from server.apps.bot_user import views


def setup_urls(app: web.Application):
    app.router.add_view("/bot_user.register", views.BotUserRegisterView)
