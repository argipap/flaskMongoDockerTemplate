import os

from flask import Flask
from project.utils.lib import cors, db, migrate


def register_blueprints(app):
    from project.views.author import authors_blueprint

    app.register_blueprint(authors_blueprint)
    from project.views.book import books_blueprint

    app.register_blueprint(books_blueprint)


def create_app(script_info=None):
    # instantiate the app
    app = Flask(__name__)

    # set config
    app_settings = os.getenv("APP_SETTINGS")
    app.config.from_object(app_settings)

    # set up extensions
    db.init_app(app)
    cors.init_app(app)
    migrate.init_app(app, db)

    # register blueprints
    register_blueprints(app)

    # shell context for flask cli
    @app.shell_context_processor
    def ctx():
        return {"app": app, "db": db}

    return app
