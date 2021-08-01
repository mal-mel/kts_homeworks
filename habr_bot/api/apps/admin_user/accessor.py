from hashlib import sha256
from datetime import datetime
from uuid import uuid4

from marshmallow_dataclass import dataclass
from marshmallow import Schema
from dataclasses import field

from typing import Type, Optional

from api.web.exceptions import AlreadyExists, InvalidCredentials


class BaseSchema:
    Schema: Type[Schema]


@dataclass
class AdminUser(BaseSchema):
    username: str
    password: str = field(metadata={"load_only": True})
    first_name: str
    last_name: str
    created: str = field(default_factory=lambda: datetime.now().isoformat())


@dataclass
class Login(BaseSchema):
    username: str
    password: str


@dataclass
class Session(BaseSchema):
    id: str
    username: str


def _get_hash(s: str) -> str:
    return sha256(s.encode()).hexdigest()


class AdminAccessor:
    def __init__(self):
        self._db = {}

    def add_user(self, user: AdminUser) -> AdminUser:
        if user.username in self._db:
            raise AlreadyExists
        self._db[user.username] = AdminUser(
            username=user.username,
            password=_get_hash(user.password),
            first_name=user.first_name,
            last_name=user.last_name
        )
        return self._db[user.username]

    def login(self, login: Login) -> AdminUser:
        if user := self._db.get(login.username):
            if user.password == _get_hash(login.password):
                return user
        raise InvalidCredentials


class SessionAccessor:
    def __init__(self):
        self._db = {}

    def generate_session(self, username: str) -> Session:
        session_id = uuid4().hex
        session = Session(session_id, username)
        self._db[session_id] = session
        return session

    def get_by_id(self, session_id: str) -> Optional[Session]:
        return self._db.get(session_id)
