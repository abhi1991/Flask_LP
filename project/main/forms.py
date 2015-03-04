# project/main/forms.py


from flask_wtf import Form
from wtforms import TextField,StringField
from wtforms.validators import DataRequired, Email, length


class SignUpForm(Form):
    name = TextField('Name', validators=[DataRequired(),length(min=4, max=25)])
    
    email = TextField(
        'Enter your email address',
        validators=[DataRequired(), Email(), length(min=3)])
    phone = StringField('Mobile',validators=[DataRequired(),length(min = 10 ,max=10,message ="Enter a valid phone number")])

