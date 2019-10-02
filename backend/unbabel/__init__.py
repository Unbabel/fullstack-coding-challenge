import os

from flask import Flask
from flask_apscheduler import APScheduler
from flask_cors import CORS
from flask_migrate import Migrate
from unbabel.config import DevelopmentConfig, ProductionConfig
from unbabel.models import db
from unbabel.utilities import update_translations

migrate = Migrate()


def create_app(development=True):
    app = Flask(__name__, instance_relative_config=True)
    CORS(app)
    app.config.from_object(ProductionConfig())

    if development:
        app.config.from_object(DevelopmentConfig())

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Add scheduler for updating incomplete translations
    scheduler = APScheduler()
    scheduler.init_app(app)
    scheduler.start()

    db.app = app
    db.init_app(app)
    with app.app_context():
        db.create_all()

    migrate.init_app(app, db)

    from . import translations
    app.register_blueprint(translations.bp)

    return app
