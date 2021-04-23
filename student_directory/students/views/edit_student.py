import os
from flask import render_template, request, redirect, url_for, flash
from flask.views import MethodView
from flask import current_app as students_app
from sqlalchemy.exc import ProgrammingError

from student_directory.app_helpers.app_helpers import AppHelpers
from student_directory.decorators import templated
from student_directory.students.forms import StudentForm
from student_directory.students.models import Student, db
from student_directory.students.state_abbrv import StateAbbrv


class EditStudent(MethodView):
    def __init__(self):
        self.edit_student_form = StudentForm()
        self.template_render_dict = dict(state_abbrv=StateAbbrv.state_abbrv_dict)

    @templated()
    def get(self, student_id):
        """

        :return:
        """
        try:
            student_object = Student.query.get(student_id)
            self.set_form_data(student_object)
            self.template_render_dict["student"] = student_object
        except ProgrammingError as pge:
            db.session.rollback()
            students_app.logger.exception(f"Error occurred with {os.environ.get('db_name')} database.")
            AppHelpers.create_flash_message(
                f"Student information could not be retrieved due to issues with database: {os.environ.get('db_name')}",
                category_request=("edit_student", "danger"))
        return self.template_render_dict

    @templated()
    def post(self, student_id):
        """

        :param student_id:
        :return:
        """

        if self.edit_student_form.delete_submit.data:
            if not self.delete(student_id):
                return redirect(url_for('edit_students', _external=True, _scheme=students_app.config.get("PREFERRED_URL_SCHEME")))
        else:
            update_student = Student.query.get(student_id)
            if self.edit_student_form.validate():
                update_student.first_name = self.edit_student_form.first_name.data
                update_student.last_name = self.edit_student_form.last_name.data
                update_student.street = self.edit_student_form.street.data
                update_student.city = self.edit_student_form.state.data
                update_student.state = self.edit_student_form.state.data
                update_student.zip = self.edit_student_form.zip.data
                db.session.commit()
            else:
                self.set_form_data(update_student)
                self.template_render_dict["student"] = update_student
                return self.template_render_dict
                # return redirect(url_for('edit_student', student_id=student_id, _external=True, _scheme=students_app.config.get("PREFERRED_URL_SCHEME")))

        return redirect(url_for('students', _external=True, _scheme=students_app.config.get("PREFERRED_URL_SCHEME")))

    def delete(self, student_id):
        """

        :param student_id:
        :return:
        """

        delete_student_obj = Student.query.get(int(student_id))
        db.session.delete(delete_student_obj)
        AppHelpers.create_flash_message(f"Student {delete_student_obj.first_name} {delete_student_obj.last_name} "
                                        f"successfully deleted.", category_request=("students", "danger"))
        db.session.commit()
        return True

    def set_form_data(self, student_obj):
        """

        :param student_obj:
        :return:
        """
        self.edit_student_form.first_name.data = student_obj.first_name
        self.edit_student_form.last_name.data = student_obj.last_name
        self.edit_student_form.street.data = student_obj.street
        self.edit_student_form.city.data = student_obj.city
        self.edit_student_form.state.data = student_obj.state
        self.edit_student_form.zip.data = student_obj.zip
        self.template_render_dict["form"] = self.edit_student_form
