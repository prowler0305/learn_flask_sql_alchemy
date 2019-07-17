import logging

from sqlalchemy import Table

from student_directory import scheduler, student_app, db
from flask_sqlalchemy import SQLAlchemy
# from student_directory.students.models import Student

logging.basicConfig()
logging.getLogger('apscheduler').setLevel(logging.INFO)

db.Model.metadata.reflect(bind=db.engine, schema='student_directory')


class Student(db.Model):
    __table__ = db.Model.metadata.tables['student']


@scheduler.task('interval', id='job1', seconds=10)
def job1():
    with student_app.app_context():
        student_app.logger.info("In scheduler job")
        print(Student.query.all())
        student_app.logger.info("leaving scheduled job")



"""
from sqlalchemy import *
from sqlalchemy.orm import create_session
from sqlalchemy.ext.declarative import declarative_base

#Create and engine and get the metadata
Base = declarative_base()
engine = create_engine('put your database connect string here')
metadata = MetaData(bind=engine)

#Reflect each database table we need to use, using metadata
class Tests(Base):
    __table__ = Table('Tests', metadata, autoload=True)

class Users(Base):
    __table__ = Table('Users', metadata, autoload=True)

#Create a session to use the tables    
session = create_session(bind=engine)

#Here I will just query some data using my foreign key relation,  as you would
#normally do if you had created a declarative data mode.
#Note that not all test records have an author so I need to accomodate for Null records
testlist = session.query(Tests).all()

for test in testlist:
    testauthor = session.query(Users).filter_by(id=test.author_id).first()
    if not testauthor:
        print "Test Name: {}, No author recorded".format(test.testname)
    else:
        print "Test Name: {}, Test Author: {}".format(test.testname, testauthor.fullname)
"""


"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'database connect url'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
db.Model.metadata.reflect(bind=db.engine,schema='DATABASE_NAME')

class User(db.Model):
    '''deal with an existing table'''
    __table__ = db.Model.metadata.tables['DATABASE_NAME.TABLE_NAME']

u = User.query.all()
print(u)
db.commit()
"""