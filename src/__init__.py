from flask import Flask
from flask_admin.contrib.sqla import ModelView

from src.config import Config
from src.ext import db, migrate, admin, dpi
from src.commands import init_db, populate_db
from src.api import UserApi
from src.models import User

COMMANDS = [init_db, populate_db]

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    register_extensions(app)

    register_commands(app)

    return app


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    admin.init_app(app)
    admin.add_views(ModelView(User, db.session))
    dpi.init_app(app)

def register_commands(app):
    for cmd in COMMANDS:
        app.cli.add_command(cmd)