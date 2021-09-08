from marshmallow_dataclass import dataclass

from datetime import time
from typing import List

from server.web.schema import BaseSchema


@dataclass
class BotUser(BaseSchema):
    user_id: int


@dataclass
class BotUserRegisterRequest(BotUser):
    username: str


@dataclass
class BotUserResponse(BotUser):
    username: str
    shedule: time


@dataclass
class BotUserGetSheduleResponse(BotUser):
    shedule: time


@dataclass
class BotUserSetSheduleRequest(BotUser):
    shedule: time


@dataclass
class BotUserTagsRequest(BotUser):
    tags: List[str]


@dataclass
class BotUserTagsResponse(BotUser):
    tags: List[str]
