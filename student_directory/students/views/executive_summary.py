import os
from flask import render_template, request, redirect, url_for, flash
from flask.views import MethodView
from flask import current_app as students_app
from student_directory import db
from student_directory.students.models import Student
from student_directory.students.state_abbrv import StateAbbrv


class ExecutiveSummary(MethodView):
    def __init__(self):
        self.template_name = 'students/executive_summary.html'
        self.student_count_by_state_dict = dict()

    def get(self):
        """

        :return:
        """
        for full_state_name, state_abbrv in StateAbbrv.state_abbrv_dict.items():
            self.student_count_by_state_dict[full_state_name] = Student.query.filter_by(state=state_abbrv).count()

        return render_template(self.template_name, total_students=Student.query.count(),
                               total_students_by_state=self.student_count_by_state_dict,
                               state_abbrv=StateAbbrv.state_abbrv_dict)