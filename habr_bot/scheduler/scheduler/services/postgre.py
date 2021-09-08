import asyncpg

from typing import Optional


class _Base:
    def __init__(self, host: str, port: int, db: str, user: str, password: str):
        self.host = host
        self.port = port
        self.db = db
        self.user = user
        self.password = password

        self._conn: Optional[asyncpg.connection.Connection] = None

    async def init(self):
        self._conn = await asyncpg.connect(host=self.host,
                                           port=self.port,
                                           database=self.db,
                                           user=self.user,
                                           password=self.password)

    async def close(self):
        await self._conn.close()


class PostgreInterface(_Base):
    async def get_user(self, user_id: int) -> dict:
        # TODO: плохой код сделать лучше
        res = {}
        user_data = await self._conn.fetchrow("""
        SELECT username, shedule FROM bot_user WHERE bot_user.user_id = $1
        """, user_id)
        if user_data:
            res.update(user_data)
            tags = await self._conn.fetch("""
            SELECT title FROM bot_user
                JOIN bot_user_tag ON id = bot_user_id
                JOIN tag t on tag_id = t.id
            WHERE bot_user.user_id = $1
            """, user_id)
            res["tags"] = []
            for t in tags:
                res["tags"].append(t["title"])
        return res
