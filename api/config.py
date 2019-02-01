import os

base_directory = os.path.abspath(os.path.dirname(__file__))


class BaseConfig():
    SECRET_KEY = os.getenv('SECRET_KEY', 'franko@pkusianwar')
    DEBUG = False


class Development(BaseConfig):
    DEBUG = True


class Production(BaseConfig):
    # heroku details
    pass


class Testing(BaseConfig):
    DEBUG = True


environments = {
    "Development": "api.config.Development",
    "Production": "api.config.Production",
    "Testing": "api.config.Testing"
}
