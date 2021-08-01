from aiohttp import web

from .views import AddUserView, LoginView


def setup_urls(app: web.Application):
    app.router.add_view("/admin_user.login", LoginView)
    app.router.add_view("/admin_user.add_user", AddUserView)
