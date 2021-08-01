from aiohttp import web

from api.apps.admin_user.urls import setup_urls as admin_user_setup_urls


def setup_urls(app: web.Application):
    admin_user_setup_urls(app)
