import os

from cbaxter1988_utils.pika_utils import make_pika_queue_consumer


def dev_make_pika_queue_consumer():
    AMQP_USER = os.getenv("AMQP_USER", 'guest')
    AMQP_PW = os.getenv("AMQP_PW", 'guest')
    AMQP_HOST = os.getenv("AMQP_HOST", '192.168.1.5')
    AMQP_PORT = os.getenv("AMQP_PORT", 5672)

    AMQP_URL = os.getenv("AMPQ_URL", f"amqp://{AMQP_USER}:{AMQP_PW}@{AMQP_HOST}:{AMQP_PORT}")

    def on_message_callback(ch, method, properties, body):
        print(ch, method, properties, body)

        if b'error' in body:
            ch.basic_nack(delivery_tag=method.delivery_tag, requeue=False)
            raise Exception("UnHanldled exception")

        ch.basic_ack(delivery_tag=method.delivery_tag)

    consumer = make_pika_queue_consumer(amqp_url=AMQP_URL, queue='TEST_QUEUE', on_message_callback=on_message_callback)

    consumer.consume(prefetch_count=1)
