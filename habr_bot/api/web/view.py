from aiohttp import web

from api.store import Store


class BaseView(web.View):
    @property
    def store(self) -> Store:
        return self.request.app["store"]
