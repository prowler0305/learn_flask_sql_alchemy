import os
from flask import render_template, request, redirect, url_for, flash
from flask.views import MethodView
from flask import current_app as students_app
from student_directory import db
from student_directory.students.models import Student
from student_directory.students.state_abbrv import StateAbbrv


class EditStudent(MethodView):
    def __init__(self):
        self.template_name = 'students/edit_student.html'

    def get(self, student_id):
        """

        :return:
        """
        return render_template(self.template_name, state_abbrv= StateAbbrv.state_abbrv_dict,
                               student=Student.query.get(student_id))

    def post(self, student_id):
        """

        :param student_id:
        :return:
        """

        if request.form.get("deleteStudentButton") is not None:
            self.delete(student_id)
        else:
            update_student = Student.query.get(student_id)
            update_student.first_name = request.form.get('first_name')
            update_student.last_name = request.form.get('last_name')
            update_student.street = request.form.get('street')
            update_student.city = request.form.get('city')
            update_student.state = request.form.get('state')
            update_student.zip = request.form.get('zipcode')
            db.session.commit()

        return redirect(url_for('students', _external=True, _scheme=students_app.config.get('PREFERRED_URL_SCHEME')))

    def delete(self, student_id):
        """

        :param student_id:
        :return:
        """

        delete_student_obj = Student.query.get(int(student_id))
        db.session.delete(delete_student_obj)
        flash("Student {} {} successfully deleted.".format(delete_student_obj.first_name, delete_student_obj.last_name))
        db.session.commit()
        return True
