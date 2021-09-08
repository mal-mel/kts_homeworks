import aio_pika
import json


class RabbitInterface:
    def __init__(self, amqp_uri: str, queue_name: str, loop):
        self.amqp_uri = amqp_uri
        self.queue_name = queue_name
        self.loop = loop

        self._connection = None
        self._channel = None
        self._queue = None

    async def init(self):
        self._connection = await aio_pika.connect_robust(self.amqp_uri,
                                                         loop=self.loop)
        self._channel = await self._connection.channel()
        self._queue = await self._channel.declare_queue(self.queue_name, auto_delete=True, durable=True)

    async def register_callback(self, callback):
        await self._queue.consume(callback)

    async def publish(self, data: dict):
        await self._channel.default_exchange.publish(aio_pika.Message(body=json.dumps(data).encode()),
                                                     routing_key=self.queue_name)

    async def close(self):
        await self._connection.close()
