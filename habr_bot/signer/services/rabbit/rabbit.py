import logging
import pika


class RabbitInterface:
    def __init__(self, amqp_uri: str, queue: str):
        self.params = pika.URLParameters(amqp_uri)
        self.queue = queue
        self._connection = None
        self._channel = None
        self._connect()

    def purge_queue(self):
        logging.info(f"purge queue: {self.queue}")
        self._channel.queue_purge(self.queue)

    @property
    def message_count(self) -> int:
        self._channel.basic_qos(prefetch_count=1)
        return self._channel.queue_declare(self.queue, durable=True).method.message_count

    def consume(self, callback):
        while True:
            try:
                self._channel.basic_consume(self.queue, callback, auto_ack=True)
                self._channel.start_consuming()
            except pika.exceptions.AMQPError as e:
                logging.exception(f'rabbit consume error: {e}')
                self._connect()

    def basic_ack(self, delivery_tag):
        self._channel.basic_ack(delivery_tag)

    def _connect(self):
        logging.info("try to connect to the rabbit")
        while True:
            try:
                self._connection = pika.BlockingConnection(self.params)
                self._channel = self._connection.channel()
                self._channel.basic_qos(prefetch_count=1)
                self._channel.queue_declare(self.queue, durable=True)
            except pika.exceptions.AMQPError as e:
                logging.exception(f"rabbit connection error: {e}")
            else:
                logging.info("rabbit connection success")
                break
