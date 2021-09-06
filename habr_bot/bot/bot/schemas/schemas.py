from datetime import time
from typing import Type
from marshmallow import Schema

from marshmallow_dataclass import dataclass


class BaseSchema:
    Schema: Type[Schema]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @property
    def json(self) -> dict:
        return self.Schema().dump(self)


@dataclass
class BaseResponse(BaseSchema):
    status: int
    data: dict


@dataclass
class BotUserRequest(BaseSchema):
    user_id: int


@dataclass
class BotUserRegister(BotUserRequest):
    username: str


@dataclass
class BotUserSetShedule(BotUserRequest):
    shedule: time
