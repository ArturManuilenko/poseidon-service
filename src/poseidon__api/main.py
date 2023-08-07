from src.conf.poseidon__api import api_sdk
from src.poseidon__api.flask import flask_app

api_sdk.load_routes()

__all__ = (
    'flask_app',
)
