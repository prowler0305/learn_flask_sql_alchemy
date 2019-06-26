import os
from flask import render_template, request, redirect, url_for, flash
from flask.views import MethodView
from flask import current_app as students_app
from student_directory import db
from student_directory.students.models import Student


class EditStudent(MethodView):
    def __init__(self):
        self.template_name = 'students/edit_student.html'

    def get(self, student_id):
        """

        :return:
        """
        return render_template(self.template_name, student=Student.query.filter_by(id=student_id).first())
