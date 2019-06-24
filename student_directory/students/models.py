from student_directory import db


class Student(db.Model):
    __tablename__ = 'student'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    street = db.Column(db.String(150))
    city = db.Column(db.String(50))
    state = db.Column(db.String(2))
    zip = db.Column(db.String(5))

    def __init__(self, first, last, street=None, city=None, zipcode=None):
        """

        :param first:
        :param last:
        :param street:
        :param city:
        :param zipcode:
        """
        self.first_name = first
        self.last_name = last
        self.street = street
        self.city = city
        self.zip = zipcode

