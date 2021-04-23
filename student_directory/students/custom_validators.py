from wtforms import ValidationError


class NoChoiceOption(object):
    def __init__(self):
        self.message = "{} is required. Value of {} is not a valid choice."

    def __call__(self, form, field):
        if field.data == "None":
            raise ValidationError(self.message.format(field.id, field.data))
