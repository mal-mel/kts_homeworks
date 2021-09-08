import asyncio
import logging

from scheduler.scheduler import Worker
from scheduler.services.rabbit import RabbitInterface
from scheduler.services.elastic import ElasticInterface
from scheduler.services.postgre import PostgreInterface

from settings import config


async def init_rabbit(loop_obj: asyncio.events.AbstractEventLoop, queue: str) -> RabbitInterface:
    logging.info(f"init rabbit, queue: {queue}")
    rab_obj = RabbitInterface(amqp_uri=config["rabbit"]["amqp_uri"],
                              queue_name=queue,
                              loop=loop_obj)
    await rab_obj.init()
    return rab_obj


def init_elastic() -> ElasticInterface:
    logging.info("init elastic")
    return ElasticInterface(host=config["elastic"]["host"],
                            port=config["elastic"]["port"],
                            index=config["elastic"]["index"])


async def init_pg() -> PostgreInterface:
    logging.info("init postgre")
    pg_obj = PostgreInterface(host=config["postgre"]["host"],
                              port=config["postgre"]["port"],
                              db=config["postgre"]["database"],
                              user=config["postgre"]["username"],
                              password=config["postgre"]["password"])
    await pg_obj.init()
    return pg_obj


async def main(loop_obj):
    rab_from = await init_rabbit(loop_obj, config["rabbit"]["queue_from"])
    rab_to = await init_rabbit(loop_obj, config["rabbit"]["queue_to"])

    es = init_elastic()
    pg = await init_pg()

    logging.info("init worker")
    worker = Worker(rab_from_obj=rab_from,
                    rab_to_obj=rab_to,
                    es_obj=es,
                    pg_obj=pg)
    await worker.start()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(main(loop))
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        loop.close()
