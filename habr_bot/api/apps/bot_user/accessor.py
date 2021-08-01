from datetime import date

from marshmallow_dataclass import dataclass
from marshmallow import Schema

from typing import List, Type

from api.web.exceptions import NotFound


class BaseSchema:
    Schema: Type[Schema]


@dataclass
class Subscriptions:
    title: str
    timing: date


@dataclass
class BotUser(BaseSchema):
    id: str
    nickname: str
    is_banned: bool
    subscriptions: List[Subscriptions]


class BotUserAccessor:
    def __init__(self):
        self._db = {}

    def list(self, limit: int, offset: int, q: str) -> List[BotUser]:
        fit_users = [u for u in self._db.values() if q in u.nickname or u.nickname in q]
        return fit_users[offset:limit]

    def get(self, _id: str) -> BotUser:
        if _id not in self._db:
            raise NotFound
        return self._db[_id]

    def update(self, _id: str,
               is_banned: bool,
               subscriptions: List[Subscriptions]) -> BotUser:

        if _id not in self._db:
            raise NotFound

        user = self._db[_id]
        user.is_banned = is_banned
        user_sub = {sub.title: sub.timing for sub in user.subscriptions}
        new_sub = {sub.title: sub.timing for sub in subscriptions}
        user_sub.update(new_sub)
        user.subscriptions = [Subscriptions(sub, timing) for sub, timing in user_sub.items()]

        return user
