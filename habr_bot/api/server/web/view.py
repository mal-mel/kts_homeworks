from aiohttp import web

from server.store import Store
from server.web.exceptions import NotAuthorized


class BaseView(web.View):
    @property
    def store(self) -> Store:
        return self.request.app["store"]


def require_auth(func):
    async def wrapper(self, *args, **kwargs):
        if not self.session:
            raise NotAuthorized
        return await func(self, *args, **kwargs)

    return wrapper
