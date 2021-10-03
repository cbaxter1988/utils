from cbaxter1988_utils import pika_utils

AMQP_USER = 'guest'
AMQP_PW = 'guest'
AMQP_HOST = '127.0.0.1'
AMQP_PORT = 5672
EXCHANGE_NAME = 'test_exchange'
ROUTING_KEY_NAME = 'test_routing_key'
QUEUE_NAME = 'QUEUE_NAME'
AMQP_URL = pika_utils.make_amqp_url(amqp_user=AMQP_USER, amqp_pw=AMQP_PW, amqp_host=AMQP_HOST, amqp_port=AMQP_PORT)

publisher = pika_utils.make_basic_pika_publisher(
    amqp_url=AMQP_URL,
    queue=QUEUE_NAME,
    exchange=EXCHANGE_NAME,
    routing_key=ROUTING_KEY_NAME
)


def message_handler(ch: BlockingChannel, method: Basic.Deliver, properties: BasicProperties, body):
    pass
    # Do Work


subscriber = pika_utils.make_basic_pika_consumer(
    amqp_url=AMQP_URL,
    queue=QUEUE_NAME,
    on_message_callback=message_handler
)

publisher.publish_message(body={"test": "data"})
subscriber.run()