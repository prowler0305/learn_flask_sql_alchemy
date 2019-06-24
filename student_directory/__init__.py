import os
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

student_app = Flask(__name__)
student_app.config.from_object(os.environ.get('app_env'))
student_app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://flask_test:uscc1234@localhost/student_directory'
student_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
student_api = Api(student_app)

db = SQLAlchemy(student_app)
from student_directory.students.views.students import Students

students_view = Students.as_view(name="students")
student_app.add_url_rule('/', view_func=students_view, methods=['GET', 'POST'])
