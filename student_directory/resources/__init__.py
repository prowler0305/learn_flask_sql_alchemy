from flask_restful import Api
from student_directory.students.resources.students import StudentListResource

def init_api() -> Api:
    """
    Initialize the Flask-Restful API with the given Flask app and register resources.
    """
    student_directory_api = Api(prefix='/api')

    # from student_directory.students.resources.students import StudentResource, StudentListResource
    student_directory_api.add_resource(StudentListResource, '/students', endpoint='student_list')
    # student_directory_api.add_resource(StudentResource, '/students/<int:student_id>', endpoint='student')

    return student_directory_api