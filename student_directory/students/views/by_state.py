import os
from flask import render_template, request, redirect, url_for, flash
from flask.views import MethodView
from flask import current_app as students_app
from student_directory import db
from student_directory.students.models import Student
from student_directory.students.state_abbrv import StateAbbrv


class ByState(MethodView):
    def __init__(self):
        self.template_name = 'students/by_state.html'

    def get(self, state):
        """

        :param state: Name of State to filter on.
        :return:
        """
        return render_template(self.template_name, state_abbrv=StateAbbrv.state_abbrv_dict,
                               students=Student.query.filter_by(state=state).all())
