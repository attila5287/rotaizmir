from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, IntegerField, SelectField, FileField
from wtforms.validators import DataRequired, Email
from flask_wtf.file import (
    FileField, FileAllowed
)

class CSVReaderForm(FlaskForm):
    csv_file = FileField(
        'Inv CSV Feed',
        validators=[
        FileAllowed(['csv'])
        ]
        )
    submit = SubmitField('Feed Inv | Read CSV')


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
                        validators=[ Email()])
    gender  = SelectField(choices=[('m', 'Male'), ('f', 'Female')], default ='m')
    is_admin  = SelectField(choices=[('n', 'NO'), ('y', 'YES')], default ='n')
    is_prez  = SelectField(choices=[('n', 'NO'), ('y', 'YES')], default ='n')
    linkedin = StringField('linkedin', default='')
    instagram = StringField('instagram', default='')
    twitter = StringField('twitter', default='')
    # picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])

class MemberEditForm(FlaskForm):
    pass
    user_id  = SelectField('UserID', choices=[('0', '0'), ('1', '1')], )
    first_name = StringField('first name', validators=[
                            DataRequired()])
     
    middle_name = StringField('middle name')
    
    last_name = StringField('last name', validators=[
                           DataRequired()],)
    phone_num = StringField('phone_number')
    email = StringField('email',
                        validators=[ Email()])
    gender  = SelectField('gender',choices=[('m', 'Male'), ('f', 'Female')], )
    is_admin  = SelectField('admin', choices=[('n', 'NO'), ('y', 'YES')], )
    is_prez  = SelectField('prez',choices=[('n', 'NO'), ('y', 'YES')], )
    img_url = StringField('image link', )
    linkedin = StringField('linkedin', )
    instagram = StringField('instagram', )
    twitter = StringField('twitter', )
    # submit = SubmitField('submit', )
    # picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])

class MemberMenu(FlaskForm):
    pass
    menu  = SelectField('Members', choices=[('0', '0'), ('1', '1')], )
    submit  = SubmitField('Show')
    # emails  = SelectField('Emails', choices=[('0', '0'), ('1', '1')], )
    

