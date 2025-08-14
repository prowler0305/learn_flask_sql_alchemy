import os
import datetime

from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore

student_app_dir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    SECRET_KEY = os.environ.get('USCC_SECRET_KEY') or 'you-will-never-guess'
    PROPAGATE_EXCEPTIONS = True
    THREADED = True
    PREFERRED_URL_SCHEME = 'https'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DB_USER = os.environ.get("db_user")
    DB_PASS = os.environ.get("db_pass")
    DB_HOST = os.environ.get("db_host", "nprdedbnas.uscc.com")
    DB_PORT = os.environ.get("db_host", "5436")
    DB_NAME = os.environ.get("db_name", "andrew_throw")
    SQLALCHEMY_DATABASE_URI = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    PORT = os.environ.get("PORT", 5000)
    HOST = os.environ.get('HOST', 'localhost')
    PREFERRED_URL_SCHEME = 'http'

    # JOBS = [
    #     {
    #         "id": "job1",
    #         "func": "jobs:job1",
    #         "trigger": "interval",
    #         "seconds": 10,
    #         "replace_existing": True
    #     }
    # ]
    # SCHEDULER_API_ENABLED = True
    # SCHEDULER_JOBSTORES = {
    #
    #     'default': SQLAlchemyJobStore(url=SQLALCHEMY_DATABASE_URI)
    #
    # }


class QaConfig(BaseConfig):
    DEBUG = True
    PORT = os.environ.get("PORT", 8080)
    HOST = os.environ.get('HOST', '0.0.0.0')


class ProductionConfig(BaseConfig):
    DEBUG = False
    PORT = os.environ.get("PORT", 8080)
    HOST = os.environ.get('HOST', '0.0.0.0')
