from unipipeline import UniPostgresWaiting

from src.conf.poseidon__db import db_config


class PoseidonDbWaiting(UniPostgresWaiting):
    def get_connection_uri(self) -> str:
        return db_config.uri
