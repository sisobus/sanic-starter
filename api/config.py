import sys
import os
from dotenv import load_dotenv
from pathlib import Path
# from datetime import timedelta

basedir = os.path.dirname(os.path.abspath(__file__))
env_path = Path(os.path.join(basedir, "..")) / '.env'
load_dotenv(dotenv_path=env_path)


def is_linux_system():
    return sys.platform == "linux" or sys.platform == "linux2"


if not is_linux_system():
    os.environ['DB_SERVICE'] = "localhost"


class BaseConfig(object):
    VERSION = os.environ['VERSION']
    SECRET_KEY = os.environ['SECRET_KEY']
    JWT_SECRET_KEY = os.environ['SECRET_KEY']
    JWT_ACCESS_TOKEN_EXPIRES = 60 * 15
    DEBUG = bool(int(os.environ['DEBUG']))
    ENV = os.environ['ENV']
    DB_NAME = os.environ['DB_NAME']
    DB_USER = os.environ['DB_USER']
    DB_PASS = os.environ['DB_PASS']
    DB_SERVICE = os.environ['DB_SERVICE']
    DB_PORT = os.environ['DB_PORT']
    SQLALCHEMY_DATABASE_URI = 'postgresql://{0}:{1}@{2}:{3}/{4}'.format(
        DB_USER, DB_PASS, DB_SERVICE, DB_PORT, DB_NAME
    )
    REDIS_NAME = os.environ['REDIS_NAME']
    REDIS_PORT = int(os.environ['REDIS_PORT'])
    SQLALCHEMY_TRACK_MODIFICATIONS = bool(int(os.environ[
        'SQLALCHEMY_TRACK_MODIFICATIONS'
    ]))
    SIGNUP_SECRET_KEY = os.environ['SIGNUP_SECRET_KEY']
    APP_PORT = os.environ['APP_PORT']
    LOGGER_ROOT_PATH = os.environ['LOGGER_ROOT_PATH']
