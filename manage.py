import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from student_directory import student_app
from student_directory import db

student_app.config.from_object(os.environ.get('app_env'))
manager = Manager(student_app)
migrate = Migrate(student_app, db)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
