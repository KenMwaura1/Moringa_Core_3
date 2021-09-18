from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Required


class ReviewForm(FlaskForm):
    title = StringField('Review Title', validators=[Required()])
    review = TextAreaField('Movie Review')
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tells us about your bio', validators=[Required()])
    submit = SubmitField('Update Profile')
