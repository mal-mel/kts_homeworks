from typing import Type
from marshmallow import Schema

from marshmallow_dataclass import dataclass


class BaseSchema:
    Schema: Type[Schema]


@dataclass
class UserBotRegister(BaseSchema):
    chat_id: int
    user_id: int
    username: str
