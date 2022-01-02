import json
import os
import threading

import pika
from cbaxter1988_utils.pika_utils import PikaQueueConsumerV2, make_pika_publisher, make_pika_service_wrapper
from pika.adapters.blocking_connection import BlockingChannel
from pika.spec import Basic, BasicProperties

AMQP_USER = os.getenv("AMQP_USER", 'guest')
AMQP_PW = os.getenv("AMQP_PW", 'guest')
AMQP_HOST = os.getenv("AMQP_HOST", '192.168.1.5')
AMQP_PORT = os.getenv("AMQP_PORT", 5672)


def dev_make_pika_queue_consumer():
    AMQP_USER = os.getenv("AMQP_USER", 'guest')
    AMQP_PW = os.getenv("AMQP_PW", 'guest')
    AMQP_HOST = os.getenv("AMQP_HOST", '192.168.1.5')
    AMQP_PORT = os.getenv("AMQP_PORT", 5672)

    AMQP_URL = os.getenv("AMPQ_URL", f"amqp://{AMQP_USER}:{AMQP_PW}@{AMQP_HOST}:{AMQP_PORT}")

    def on_message_callback(ch: BlockingChannel, method: Basic.Deliver, properties: BasicProperties, body: bytes):
        print("thread_id", threading.get_ident())
        print(ch, method.delivery_tag, body)
        if b'error' in body:
            ch.basic_nack(delivery_tag=method.delivery_tag, requeue=False)
            raise Exception("UnHanldled exception")

        ch.basic_ack(method.delivery_tag)

    # consumer = make_pika_queue_consumer(amqp_url=AMQP_URL, queue='TEST_QUEUE', on_message_callback=on_message_callback)
    consumer = PikaQueueConsumerV2(
        amqp_host='192.168.1.5',
        amqp_username='guest',
        amqp_password='guest',
        callback=on_message_callback,
        queue_name='TEST_QUEUE',
        heartbeat=0
    )
    consumer.consume(prefetch_count=10)


def dev_make_pika_publisher():
    publisher = make_pika_publisher(
        amqp_host=AMQP_HOST,
        amqp_password=AMQP_PW,
        amqp_username=AMQP_USER
    )

    publisher.publish_message(
        exchange='TEST_EXCHANGE',
        routing_key='TEST_QUEUE',
        properties=pika.BasicProperties(content_type='application/json'),
        body=json.dumps({"msg": "test message"})

    )


def dev_make_pika_service_wrapper():
    service_wrapper = make_pika_service_wrapper(
        amqp_host=AMQP_HOST,
        amqp_username=AMQP_USER,
        amqp_password=AMQP_PW,
    )

    service_wrapper.create_queue(
        queue="TEST_QUEUE_2",
        dlq_support=True,
        dlq_queue='TEST_DLQ_QUEUE',
        dlq_exchange='TEST_DLQ_EXCHANGE',
        dlq_routing_key='TEST_DLQ_ROUTING_KEY'
    )

    #
    # service_wrapper.delete_queue(queue='TEST_DLQ_QUEUE')

# dev_make_pika_service_wrapper()
# dev_make_pika_queue_consumer()
