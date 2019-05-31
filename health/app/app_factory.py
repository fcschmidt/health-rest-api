import logging
from health.settings import app_config
from flask import Flask


def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(app_config[config_name])

    # Initialize Extensions
    register_extensions(app)

    # Initialize Blueprints
    register_blueprints(app)

    # Initialize Logs
    register_logs(app)

    return app


def register_blueprints(app):
    """Register Blueprints"""
    from health.app.blueprints.api.prescriptions import resource as prescription_api

    prescription_api.init_app(app)
    return app


def register_extensions(app):
    """Register extensions."""
    from health.app.ext.db import db
    from health.app.ext.migrate import migrate

    db.init_app(app)
    migrate.init_app(app, db)
    return app


def register_logs(app):
    """Register logs."""
    logging.basicConfig(
        filename='logs/app.logs',
        level=logging.DEBUG,
        format='[%(asctime)s]:%(levelname)s:%(message)s'
    )
    return app
