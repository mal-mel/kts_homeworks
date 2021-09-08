from aiohttp import web

from aiohttp_apispec import setup_aiohttp_apispec, validation_middleware

from server.store import Store
from server.web.middlewares import error_middleware, resp_middleware, auth_mw
from server.web.urls import setup_urls


middlewares = [
    error_middleware,
    validation_middleware,
    resp_middleware,
    auth_mw
]


def setup_store(app: web.Application):
    store = Store(app)
    app["store"] = store
    store.setup()


def create_app():
    app = web.Application(
        middlewares=middlewares
    )
    setup_store(app)
    setup_urls(app)
    setup_aiohttp_apispec(
        app=app,
        title="My Documentation",
        version="v1",
        swagger_path="/api/docs",
    )
    return app
