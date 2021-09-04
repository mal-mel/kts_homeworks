from marshmallow_dataclass import dataclass

from server.web.schema import BaseSchema


@dataclass
class BotUserRegisterRequest(BaseSchema):
    user_id: int
    chat_id: int
    username: str


@dataclass
class BotUserResponse(BaseSchema):
    user_id: int
    chat_id: int
    username: str
