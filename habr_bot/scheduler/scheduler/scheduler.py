import aio_pika
import asyncio
import json
import logging

from datetime import datetime, timedelta
from dateutil import parser as dt_parser

from typing import Dict

from scheduler.services.elastic import ElasticInterface
from scheduler.services.postgre import PostgreInterface
from scheduler.services.rabbit import RabbitInterface
from scheduler.watchdog import watchdog


class Worker:
    def __init__(self,
                 rab_from_obj: RabbitInterface,
                 rab_to_obj: RabbitInterface,
                 es_obj: ElasticInterface,
                 pg_obj: PostgreInterface):
        self.rab_from_obj = rab_from_obj
        self.rab_to_obj = rab_to_obj
        self.es_obj = es_obj
        self.pg_obj = pg_obj

        self._workers: Dict[int, asyncio.Task] = {}
        self._ids = set()

    async def start(self):
        logging.info("start consumer")
        await self.rab_from_obj.register_callback(self._consume)

    async def _consume(self, message: aio_pika.IncomingMessage):
        """
        data = {
            "user_id": 341657381,
            "schedule": "13:00"
        }

        :param message:
        :return:
        """
        # TODO: сделать нормальную валидацию
        async with message.process():
            logging.info(f"get new event: {message.body}")
            data = json.loads(message.body)
            if "user_id" in data and "schedule" in data:
                user_id, schedule_s = data["user_id"], data["schedule"]
                schedule = dt_parser.parse(schedule_s)
                if user_id in self._workers:
                    logging.info(f"cancel worker for user: {user_id}")
                    self._workers[user_id].cancel()
                logging.info(f"create worker for user: {user_id}")
                self._workers[user_id] = asyncio.create_task(self._worker(user_id, schedule))

    @watchdog
    async def _worker(self, user_id: int, schedule: datetime):
        # TODO: сделать нормальный шедулер
        while True:
            current_t = datetime.now()
            if schedule < current_t:
                schedule += timedelta(days=1)
            td = schedule - current_t
            logging.info(f"sleep {td.seconds} seconds for user: {user_id}")
            await asyncio.sleep(td.seconds)
            logging.info(f"get data for user: {user_id}")
            user_data = await self.pg_obj.get_user(user_id)
            if tags := user_data.get("tags"):
                logging.info(f"search articles for user: {user_id}, tags: {tags}")
                articles = await self.es_obj.search_articles(tags)
                logging.info(f"articles found [{len(articles)}], push to bot for user: {user_id}")
                await self.rab_to_obj.publish({
                        "user_id": user_id,
                        "urls": [art["url"] for art in articles]
                    })
            await asyncio.sleep(10)
