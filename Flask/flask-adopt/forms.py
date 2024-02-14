from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField, SelectField, TextAreaField
from wtforms.validators import InputRequired, Optional, URL, NumberRange


class AddPetForm(FlaskForm):
    """Form for adding a new pet."""
    name = StringField("Pet Name", validators=[InputRequired(message="Don't forget the pet's name!")])
    species = SelectField("Pet Species", choices=[("cat", "Cat"), ("dog", "Dog"), ("porcupine", "Porcupine")])
    photo_url = StringField("Pet Photo", validators=[Optional(), URL()])
    age = IntegerField("Pet Age", validators=[Optional(), NumberRange(min=0, max=30)])
    notes = TextAreaField("Pet Notes", validators=[Optional()])

class EditPetForm(FlaskForm):
    """Form for editing a pet."""
    photo_url = StringField("Pet Photo", validators=[Optional(), URL()])
    notes = StringField("Pet Notes", validators=[Optional()])
    available = BooleanField("Available?")   