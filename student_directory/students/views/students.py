import os
from flask import render_template, request, redirect, url_for, flash, current_app as student_app
from flask.views import MethodView
from flask import current_app as students_app
from sqlalchemy.exc import ProgrammingError
from student_directory.app_helpers.app_helpers import AppHelpers

from student_directory import db
from student_directory.decorators import templated
from student_directory.students.forms import StudentForm
from student_directory.students.models import Student
from student_directory.students.state_abbrv import StateAbbrv


class Students(MethodView):
    def __init__(self):
        self.add_student_form = StudentForm()
        self.template_render_dict = dict(form=self.add_student_form, state_abbrv=StateAbbrv.state_abbrv_dict)

    @templated()
    def get(self):
        """

        :return:
        """
        # try:
        #     list_o_students = Student.query.all()
        # except ProgrammingError as prog_err:
        #     students_app.logger.exception(f"Error occurred with {student_app.config.get('DB_NAME')} database.")
        #     list_o_students = []
        #     db.session.rollback()
        #     AppHelpers.create_flash_message(
        #         f"Student information could not be retrieved due to issues with database: {student_app.config.get('DB_NAME')}",
        #         category_request=("students", "danger"))
        # self.template_render_dict["students"] = list_o_students

        return self.template_render_dict

    @templated()
    def post(self):
        """

        :return:
        """
        if self.add_student_form.validate_on_submit():
            try:
                new_student = Student(self.add_student_form.first_name.data, self.add_student_form.last_name.data,
                                      self.add_student_form.street.data, self.add_student_form.city.data,
                                      self.add_student_form.state.data, self.add_student_form.zip.data)

                db.session.add(new_student)
                db.session.commit()
                AppHelpers.create_flash_message(f"New student {request.form.get('first_name')} {request.form.get('last_name')} successfully added",
                                                category_request=("students", "info"))
            except ProgrammingError as pge:
                students_app.logger.exception(f"Error occurred with {student_app.config.get('DB_NAME')} database.")
                AppHelpers.create_flash_message(f"Student {request.form.get('first_name')} {request.form.get('last_name')} not added due to internal error",
                                                category_request=("students", "danger"))

            return redirect(url_for('students', _external=True, _scheme=students_app.config.get('PREFERRED_URL_SCHEME')))
        else:
            return self.template_render_dict
