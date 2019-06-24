from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from student_directory import student_app
from student_directory import db

manager = Manager(student_app)
migrate = Migrate(student_app, db)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
