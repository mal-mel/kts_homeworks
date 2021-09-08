from server.store.gino import db


class BotUser(db.Model):
    __tablename__ = "bot_user"

    id = db.Column(db.Integer(), primary_key=True, unique=True, nullable=False, autoincrement=True)
    user_id = db.Column(db.Integer(), unique=True, nullable=False)
    username = db.Column(db.Text(), nullable=False)
    shedule = db.Column(db.Time())

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._tags = set()

    @property
    def tags(self) -> set:
        return self._tags

    def add_tag(self, tag: 'Tag'):
        self._tags.add(tag.title)


class Tag(db.Model):
    __tablename__ = "tag"

    id = db.Column(db.Integer(), primary_key=True, unique=True, nullable=False, autoincrement=True)
    title = db.Column(db.String(512), nullable=False, unique=True)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._users = set()

    @property
    def users(self) -> set:
        return self._users


class BotUserXTag(db.Model):
    __tablename__ = "bot_user_tag"

    bot_user_id = db.Column(db.Integer, db.ForeignKey("bot_user.id"))
    tag_id = db.Column(db.Integer, db.ForeignKey("tag.id"))
