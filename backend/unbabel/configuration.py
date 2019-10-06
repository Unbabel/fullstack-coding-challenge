import os

base_dir = os.path.abspath(os.path.dirname(__file__))


class Configuration(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
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


class ProductionConfiguration(Configuration):
    DEBUG = False
    TESTING = False


class DevelopmentConfiguration(Configuration):
    DEBUG = True


class TestingConfiguration(Configuration):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL_TESTING")
