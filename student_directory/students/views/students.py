import os
from flask import render_template, request, redirect, url_for, flash
from flask.views import MethodView
from flask import current_app as students_app

from student_directory import db
from student_directory.students.models import Student
from student_directory.students.state_abbrv import StateAbbrv


class Students(MethodView):
    def __init__(self):
        self.template_name = 'students/students_home.html'

    def get(self):
        """

        :return:
        """
        return render_template(self.template_name, state_abbrv=StateAbbrv.state_abbrv_dict,
                               students=Student.query.all())

    def post(self):
        """

        :return:
        """
        new_student = Student(request.form.get('first_name'), request.form.get('last_name'), request.form.get('street'),
                              request.form.get('city'), request.form.get('state'), request.form.get('zipcode'))

        db.session.add(new_student)
        db.session.commit()
        flash("New student {} {} successfully added".format(request.form.get('first_name'), request.form.get('last_name')))
        return redirect(url_for('students'))
