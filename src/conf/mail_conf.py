import os


class MailConfig(object):
    MAIL_SERVER = os.environ['POSEIDON__MAIL_SERVER']
    MAIL_USERNAME = os.environ['POSEIDON__MAIL_USERNAME']
    MAIL_PASSWORD = os.environ['POSEIDON__MAIL_PASSWORD']
    MAIL_PORT = os.environ['POSEIDON__MAIL_PORT']
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
