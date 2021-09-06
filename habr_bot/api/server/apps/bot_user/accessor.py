from datetime import time

from server.store.gino import db
from server.apps.bot_user.models import BotUser, Tag, BotUserXTag
from server.store.accessor import Accessor
from server.web.exceptions import AlreadyExists, NotFound


class BotUserAccessor(Accessor):
    @staticmethod
    async def register_user(user_id: int, username: str) -> BotUser:
        user = await BotUser.query.where(BotUser.user_id == user_id).gino.first()
        if user:
            raise AlreadyExists
        return await BotUser.create(user_id=user_id, username=username)

    @staticmethod
    async def get_user(user_id: int) -> BotUser:
        user = await BotUser.query.where(BotUser.user_id == user_id).gino.first()
        if not user:
            raise NotFound
        return user

    @staticmethod
    async def set_shedule(user_id: int, shedule: time) -> BotUser:
        user = await BotUser.query.where(BotUser.user_id == user_id).gino.first()
        if not user:
            raise NotFound
        await user.update(shedule=shedule).apply()
        return user

    @staticmethod
    async def get_tags(user_id: int):
        query = BotUser.outerjoin(BotUserXTag).outerjoin(Tag).select()
        tags = await query.gino.load(BotUser.distinct(BotUser.id).load(add_tag=Tag.distinct(Tag.id))).query.where(BotUser.user_id == user_id).gino.all()
        if not tags:
            raise NotFound
        return tags

    @staticmethod
    async def add_tags(user_id: int, tags: list) -> BotUser:
        user = await BotUser.query.where(BotUser.user_id == user_id).gino.first()
        if not user:
            raise NotFound
        for tag in tags:
            db_tag = await Tag.query.where(Tag.title == tag).gino.first()
            if not db_tag:
                db_tag = await Tag.create(title=tag)
            query = db.text("SELECT * FROM bot_user_tag WHERE bot_user_id = :user_id AND tag_id = :tag_id")
            rel = await db.first(query, user_id=user.id, tag_id=db_tag.id)
            if not rel:
                await BotUserXTag.create(bot_user_id=user.id, tag_id=db_tag.id)
        return user
