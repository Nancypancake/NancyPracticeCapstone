# This file is where data entry forms are created. Forms are placed on templates 
# and users fill them out.  Each form is an instance of a class. Forms are managed by the 
# Flask-WTForms library.

from flask_wtf import FlaskForm
import mongoengine.errors
from wtforms.validators import URL, Email, DataRequired, NumberRange
from wtforms.fields.html5 import URLField, DateField, IntegerRangeField, EmailField
from wtforms import StringField, SubmitField, TextAreaField, IntegerField, SelectField, FileField, RadioField
from wtforms_components import TimeField

class ProfileForm(FlaskForm):
    fname = StringField('First Name', validators=[DataRequired()])
    lname = StringField('Last Name', validators=[DataRequired()]) 
    image = FileField("Image") 
    role = SelectField('Role', choices=[('Creator','Creator'),('Client','Client')])
    age = IntegerField('Age', validators=[DataRequired()])
    submit = SubmitField('Post')

class ConsentForm(FlaskForm):
    adult_fname = StringField('First Name',validators=[DataRequired()])
    adult_lname = StringField('Last Name',validators=[DataRequired()])
    adult_email = EmailField('Email',validators=[Email()])
    consent = RadioField('Do you want your parents or teachers to see your sleep data/graph', choices=[(True,"True"),(False,"False")])
    submit = SubmitField('Submit')

class StatusForm(FlaskForm):
    mood = SelectField('Rate your emotional state from 1 (lowest-- terrible) to 5 (highest-- amazing)', choices=[(None,'---'),(1,1),(2,2),(3,3),(4,4),(5,5)], validators=[DataRequired()])
    note = TextAreaField('Free Space to explain your state', validators=[DataRequired()])
    favorite = StringField('Mention one thing you really like!', validators=[DataRequired()])
    submit = SubmitField("Submit")


class BlogForm(FlaskForm):
    subject = StringField('Subject', validators=[DataRequired()])
    content = TextAreaField('Blog', validators=[DataRequired()])
    tag = StringField('Tag', validators=[DataRequired()])
    submit = SubmitField('Blog')

class CommentForm(FlaskForm):
    content = TextAreaField('Comment', validators=[DataRequired()])
    submit = SubmitField('Comment')