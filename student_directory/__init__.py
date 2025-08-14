import os
import logging
import sys

from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_restful import Api
from flask_script import Manager, Server
from flask_sqlalchemy import SQLAlchemy

from student_directory.resources import init_api
# from flask_apscheduler import APScheduler
# from student_directory import jobs
from student_directory.students.models import db


def create_app():
    student_app = Flask(__name__)
    student_app.config.from_object(os.environ.get('app_env'))
    db.init_app(student_app)
    manager = Manager(student_app)
    migrate = Migrate(student_app, db)
    manager.add_command('db', MigrateCommand)
    # scheduler = APScheduler()
    # scheduler.init_app(student_app)
    # scheduler.start()
    if 'runserver' in sys.argv:
        manager.add_command('runserver', Server(use_debugger=student_app.config.get('DEBUG'),
                                                threaded=student_app.config.get('THREADED'), port=student_app.config.get('PORT'),
                                                host=student_app.config.get('HOST'),
                                                use_reloader=student_app.config.get('USE_RELOADER')))
    with student_app.app_context():
        from . import routes
    init_api().init_app(student_app)

    return manager
