from os import getenv
from health.app.app_factory import create_app

app = create_app(getenv('FLASK_ENV') or 'default')
