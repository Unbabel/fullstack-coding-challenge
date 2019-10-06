from dotenv import load_dotenv
from flask import Flask
from flask_apscheduler import APScheduler
from flask_cors import CORS
from flask_migrate import Migrate
from unbabel.configuration import ProductionConfiguration, TestingConfiguration
from unbabel.models import db
from unbabel.utilities import update_translations

load_dotenv()

migrate = Migrate()


def create_app(testing=False):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(ProductionConfiguration())
    CORS(app)

    if testing:
        app.config.from_object(TestingConfiguration())

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
