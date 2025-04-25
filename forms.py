from flask_wtf import FlaskForm
from wtforms import SubmitField, IntegerField, FloatField, BooleanField, StringField
from wtforms.validators import DataRequired, NumberRange

class AddMovieForm(FlaskForm):
    title = StringField("Movie name", validators=[DataRequired()])
    genre = StringField("Genre")
    year = IntegerField("Year of production", validators=[NumberRange(min=1888, max=2100)])
    rating = FloatField("Score", validators=[NumberRange(min=0, max=10)])
    watched = BooleanField("Have I watched ?")
    submit = SubmitField("Add")