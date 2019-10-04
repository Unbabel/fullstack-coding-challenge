import os

base_dir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.environ["DATABASE_URI"]
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JOBS = [
        {
            "id": "update_translations",
            "func": "unbabel.utilities:update_translations",
            "trigger": "interval",
            "seconds": 10
        }
    ]
    SCHEDULER_API_ENABLED = True


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
