import os

from db_utils import DbConfig


db_config = DbConfig(
    uri=os.environ['POSEIDON__DB_URI'],
)
