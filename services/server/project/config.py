import os


class BaseConfig:
    """Base configuration"""

    TESTING = False
    SECRET_KEY = os.environ.get("SECRET_KEY")
    MONGOALCHEMY_SERVER_AUTH = False
    MONGOALCHEMY_SERVER = os.environ.get("MONGOALCHEMY_SERVER")
    MONGOALCHEMY_PORT = os.environ.get("MONGOALCHEMY_PORT")


class DevelopmentConfig(BaseConfig):
    """Development configuration"""

    MONGOALCHEMY_DATABASE = os.environ.get("MONGOALCHEMY_DATABASE")


class TestingConfig(BaseConfig):
    """Testing configuration"""

    TESTING = True
    MONGOALCHEMY_DATABASE = os.environ.get("MONGOALCHEMY_DATABASE_TEST")


class StagingConfig(BaseConfig):
    """Staging configuration"""

    MONGOALCHEMY_DATABASE = os.environ.get("MONGOALCHEMY_DATABASE")


class ProductionConfig(BaseConfig):
    """Production configuration"""

    DEBUG = False
    MONGOALCHEMY_DATABASE = os.environ.get("MONGOALCHEMY_DATABASE")
