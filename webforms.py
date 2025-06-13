from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Regexp

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    message = TextAreaField('Message', validators=[DataRequired()])
    submit = SubmitField('Send')
    
    
# class ContactForm(FlaskForm):
#     name = StringField('Name', validators=[DataRequired(message="Please enter your name.")])
#     email = StringField('Email', validators=[
#         DataRequired(message="Please enter your email."),
#         Email(message="Please enter a valid email address (e.g., user@domain.com)."),
#         Regexp(
#             r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
#             message="Please enter a valid email address (e.g., user@domain.com)."
#         )
#     ])
#     message = TextAreaField('Message', validators=[DataRequired(message="Please enter your message.")])
#     submit = SubmitField('Send Message')