import os

from unipipeline import Uni

import src.conf.self_logging  # noqa: F401

CONFIG_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dag.yml")

uni = Uni(CONFIG_FILE)
