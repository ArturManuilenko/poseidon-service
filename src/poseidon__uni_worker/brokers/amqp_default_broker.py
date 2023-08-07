from unipipeline import UniAmqpBroker

from src.conf.poseidon_input_worker import POSEIDON__AMQP_BROKER__URI


class DefaultAmqpBroker(UniAmqpBroker):

    @classmethod
    def get_connection_uri(cls) -> str:
        return POSEIDON__AMQP_BROKER__URI
