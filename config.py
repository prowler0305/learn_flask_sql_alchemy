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


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    PORT = 5000 if os.environ.get("PORT") is None else int(os.environ.get("PORT"))
    HOST = os.environ.get('HOST') or 'localhost'
    PREFERRED_URL_SCHEME = 'http'
    SQLALCHEMY_DATABASE_URI = 'postgresql://{}:{}@{}:{}/{}'.format(os.environ.get('db_user'), os.environ.get('db_pass'),
                                                                   os.environ.get('db_url'), os.environ.get('db_port'),
                                                                   os.environ.get('db_name'))
    # JOBS = [
    #     {
    #         "id": "job1",
    #         "func": "jobs:job1",
    #         "trigger": "interval",
    #         "seconds": 10,
    #         "replace_existing": True
    #     }
    # ]
    SCHEDULER_API_ENABLED = True
    SCHEDULER_JOBSTORES = {

        'default': SQLAlchemyJobStore(url=SQLALCHEMY_DATABASE_URI)

    }


class QaConfig(BaseConfig):
    DEBUG = True
    PORT = 8080 if os.environ.get("PORT") is None else int(os.environ.get('PORT'))
    HOST = os.environ.get('HOST') or '0.0.0.0'
    SQLALCHEMY_DATABASE_URI = 'postgresql://{}:{}@{}:{}/{}'.format(os.environ.get('db_user'), os.environ.get('db_pass'),
                                                                   os.environ.get('db_url'), os.environ.get('db_port'),
                                                                   os.environ.get('db_name'))


class ProductionConfig(BaseConfig):
    DEBUG = False
    PORT = 8080 if os.environ.get("PORT") is None else int(os.environ.get('PORT'))
    HOST = os.environ.get('HOST') or '0.0.0.0'
    SQLALCHEMY_DATABASE_URI = 'postgresql://{}:{}@{}:{}/{}'.format(os.environ.get('db_user'), os.environ.get('db_pass'),
                                                                   os.environ.get('db_url'), os.environ.get('db_port'),
                                                                   os.environ.get('db_name'))
