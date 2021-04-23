from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField
from wtforms.validators import InputRequired

from student_directory.students.custom_validators import NoChoiceOption
from student_directory.students.state_abbrv import StateAbbrv


class StudentForm(FlaskForm):
    first_name = StringField("First", validators=[InputRequired()])
    last_name = StringField("Last", validators=[InputRequired()])
    street = StringField("Street", validators=[InputRequired()])
    city = StringField("City", validators=[InputRequired()])
    state = SelectField("State", choices=StateAbbrv.generate_state_choices(), validators=[NoChoiceOption()])
    zip = StringField("Zipcode", validators=[InputRequired()])
    add_submit = SubmitField("Add")
    update_submit = SubmitField("Update")
    delete_submit = SubmitField("Delete")

