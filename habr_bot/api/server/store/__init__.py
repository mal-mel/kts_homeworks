from aiohttp import web


class Store:
    def __init__(self, app: web.Application):
        from server.store.pg import PgAccessor
        from server.store.gino import GinoAccessor
        self.pg = PgAccessor(app)
        self.gino = GinoAccessor(app)

        from server.apps.admin_user.accessor import AdminUserAccessor
        self.admin_user = AdminUserAccessor(app)

        from server.apps.bot_user.accessor import BotUserAccessor
        self.bot_user = BotUserAccessor(app)

    def setup(self, ):
        self.pg.setup()
        self.gino.setup()
