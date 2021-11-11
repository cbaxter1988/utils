from cbaxter1988_utils import environment_utils
from cbaxter1988_utils import pika_utils
from pika.adapters.blocking_connection import BlockingChannel
from pika.spec import Basic, BasicProperties
from cbaxter1988_utils.src.models.factory import Factory, ValueObject
from dataclasses import dataclass

model_factory = Factory()

def pika_example():
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


def eviornment_example_1():
    var = environment_utils.get_env_strict("AWS_REGION")

    # Gets env with side-effect
    try:
        var = environment_utils.get_env_strict(key="AWS_REGION")
    except KeyError:
        raise

    # Gets env
    var = environment_utils.get_env(key="AWS_REGION", default_value="us-east-1")

    # Sets env
    environment_utils.set_env(key="AWS_REGION", val="us-west-1")

def value_object_example():
    @dataclass(frozen=True)
    class PersonValueObject(ValueObject):
        first_name: str
        last_name: str

    data = {
        "first_name": "courtney",
        "last_name": "baxter",
    }
    # value_object = model_factory.make_value_object(**data)
    # print(value_object)
    value_object = PersonValueObject(**data)
    assert isinstance(value_object, ValueObject)

    print(value_object)
value_object_example()