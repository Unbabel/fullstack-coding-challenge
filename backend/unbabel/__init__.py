import os

from flask import Flask
from flask_migrate import Migrate
from unbabel.config import DevelopmentConfig, ProductionConfig
from unbabel.models import db

migrate = Migrate()


def create_app(development=True):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(ProductionConfig())

    if development:
        app.config.from_object(DevelopmentConfig())

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db.init_app(app)
    with app.app_context():
        db.create_all()

    migrate.init_app(app, db)

    @app.route("/")
    def hello():
        return "Hello, World!"

    from . import translations
    app.register_blueprint(translations.bp)

    return app
