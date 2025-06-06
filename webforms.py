from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(message="Please enter your name.")])
    email = StringField('Email', validators=[DataRequired(message="Please enter your email."), Email(message="Please enter a valid email address.")])
    message = TextAreaField('Message', validators=[DataRequired(message="Please enter your message.")])
    submit = SubmitField('Send Message')
    