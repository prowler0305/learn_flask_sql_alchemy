import os
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

student_app = Flask(__name__)
student_app.config.from_object(os.environ.get('app_env'))
student_api = Api(student_app)

db = SQLAlchemy(student_app)
from student_directory.students.views.students import Students
from student_directory.students.views.edit_student import EditStudent
from student_directory.students.views.executive_summary import ExecutiveSummary
from student_directory.students.views.by_state import ByState

students_view = Students.as_view(name="students")
edit_student_view = EditStudent.as_view(name='edit_student')
executive_summary = ExecutiveSummary.as_view(name='executive')
by_state_view = ByState.as_view(name='by_state')
student_app.add_url_rule('/', view_func=students_view, methods=['GET', 'POST'])
student_app.add_url_rule('/student/<student_id>', view_func=edit_student_view, methods=['GET', 'POST'])
student_app.add_url_rule('/executive', view_func=executive_summary)
student_app.add_url_rule('/by_state/<state>', view_func=by_state_view)
