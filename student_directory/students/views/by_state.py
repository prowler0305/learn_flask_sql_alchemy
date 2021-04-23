import os
from flask import render_template, request, redirect, url_for, flash
from flask.views import MethodView
from flask import current_app as students_app
from sqlalchemy.exc import ProgrammingError

from student_directory.app_helpers.app_helpers import AppHelpers
from student_directory.decorators import templated
from student_directory.students.models import Student, db
from student_directory.students.state_abbrv import StateAbbrv


class ByState(MethodView):
    def __init__(self):
        self.template_render_dict = dict(state_abbrv=StateAbbrv.state_abbrv_dict)

    @templated()
    def get(self, state):
        """

        :param state: Name of State to filter on.
        :return:
        """
        try:
            self.template_render_dict["students"] = Student.query.filter_by(state=state).all()
        except ProgrammingError as prog_err:
            students_app.logger.exception(f"Error occurred with {os.environ.get('db_name')} database.")
            db.session.rollback()
            AppHelpers.create_flash_message(
                f"Information could not be retrieved due to issues with database: {os.environ.get('db_name')}",
                category_request=("students", "danger"))
        return self.template_render_dict
