from flask import current_app as student_app
from student_directory.students.models import Student


def job1():
    student_app.logger.info("In scheduled job")
    with student_app.app_context():
        student_app.logger.info("In scheduler job")
        student_app.logger.info(Student.query.all())
        student_app.logger.info("leaving scheduled job")
