from aiohttp import web
from aiohttp_apispec import setup_aiohttp_apispec, validation_middleware

from api.store import Store

from .urls import setup_urls
from .middlewares import error_middleware, resp_middleware


_MIDDLEWARES = [
    validation_middleware,
    error_middleware,
    resp_middleware
]


def create_app(_) -> web.Application:
    app = web.Application(middlewares=_MIDDLEWARES)

    app["store"] = Store()

    setup_urls(app)
    setup_aiohttp_apispec(
        app=app,
        title="Api Doc",
        version="v1",
        swagger_path="/api/docs",
    )

    return app
