from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, IntegerField, SelectField
from wtforms.validators import DataRequired, Email


class MemberForm(FlaskForm):
    pass
    user_id = IntegerField('UserID')
    
    first_name = StringField('first name', validators=[
                            DataRequired()], default='Attila')
     
    middle_name = StringField('middle name', default='')
    
    last_name = StringField('last name', validators=[
                           DataRequired()], default='Turkoz')
    phone_num = StringField('phone_number', default='')
    email = StringField('email',
                        validators=[DataRequired(), Email()])
    gender  = SelectField(choices=[('m', 'Male'), ('f', 'Female')], default ='m')
    is_admin  = SelectField(choices=[('n', 'NO'), ('y', 'YES')], default ='n')
    is_member  = SelectField(choices=[('n', 'NO'), ('y', 'YES')], default ='n')
    is_prez  = SelectField(choices=[('n', 'NO'), ('y', 'YES')], default ='n')

