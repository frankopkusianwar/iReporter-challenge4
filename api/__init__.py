import os
from flask import Flask
from flask_cors import CORS
from api.config import environments

def create_app(environ_name):
    app = Flask(__name__, instance_relative_config=True)
    CORS(app)
    settings = os.getenv("ENV_SETTINGS", environments[environ_name])
    app.config.from_object(settings)
    from api.views import views
    app.register_blueprint(views.bp)
    return app

