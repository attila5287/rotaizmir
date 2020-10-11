from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class Member(FlaskForm):
    pass
    user_id = IntegerField('UserID',default=0)
    
    first_name = StringField('first name', validators=[
                            DataRequired()], default='Attila')
     
    middle_name = StringField('middle name', default='')
    
    last_name = StringField('last name', validators=[
                           DataRequired()], default='Turkoz')
    phone_number = StringField('phone_number', default='')
    email = StringField('email',
                        validators=[DataRequired(), Email()])
    gender  = SelectField(choices=[('m', 'Male'), ('f', 'Female')], default ='m')
    is_admin  = SelectField(choices=[('n', 'NO'), ('y', 'YES')], default ='n')
    is_member  = SelectField(choices=[('n', 'NO'), ('y', 'YES')], default ='n')
    is_prez  = SelectField(choices=[('n', 'NO'), ('y', 'YES')], default ='n')


class PostDemo():
    ''' create post obj for demo purpose no db backup for these items '''
    date_posted = datetime.utcnow().date()
    user_id = '00'
    author = 'attila'

    def __init__(self, title='demo title', content='demo content'):
        self.title = title
        self.content = content
        print(self)

    def __repr__(self):
        return f"PostDemo('\n...{self.title}'\n\t '{self.content}')"
