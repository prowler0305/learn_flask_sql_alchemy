import os
import logging
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_apscheduler import APScheduler
# from student_directory import jobs
from student_directory.students.models import db


def create_app():
    student_app = Flask(__name__)
    student_app.config.from_object(os.environ.get('app_env'))
    db.init_app(student_app)
    # scheduler = APScheduler()
    # scheduler.init_app(student_app)
    # scheduler.start()
    student_api = Api(student_app)

    with student_app.app_context():
        from . import routes

    return student_app
