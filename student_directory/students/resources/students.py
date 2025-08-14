from flask_restful import Resource
from flask import current_app as student_app
from sqlalchemy.exc import ProgrammingError

from student_directory.students.models import Student, db


class StudentListResource(Resource):
    """Resource for handling student list operations."""

    def get(self):
        """
        Retrieve the list of students.

        :return: List of students.
        """
        try:
            list_o_students = Student.query.all()
        except ProgrammingError as prog_err:
            student_app.logger.exception(f"Error occurred with {student_app.config.get('DB_NAME')} database.")
            list_o_students = []
            db.session.rollback()
            return {'error': str(prog_err)}, 500

        return [{k: v for k, v in student.__dict__.items() if not k.startswith('_')} for student in list_o_students], 200