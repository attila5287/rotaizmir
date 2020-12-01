from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, IntegerField, SelectField, FileField
from wtforms.validators import DataRequired, Email
from flask_wtf.file import (
    FileField, FileAllowed
)

class UserMenu(FlaskForm):
    pass
    menu  = SelectField('Users', choices=[('0', '0'), ('1', '1')], )
    
class TableModeSelect(FlaskForm):
    pass
    mode  = SelectField('Table: ', 
                        choices=[
                            (0, 'default'), 
                            ], 
                        default= 0,
                        )
    submit = SubmitField('Mode ON')

class AdminNoteForm(FlaskForm):
    status = SelectField('',
                        choices=[
                            ('pending', 'approved', ), 
                            ('approved', 'approved', ), 
                            ('declined', 'declined', ), 
                            ('in review','in review', ), 
                            ], 
                        default= 'member',
                           )
    category = SelectField('',
                        choices=[
                            ('member', 'member', ), 
                            ('admin', 'admin', ), 
                            ('prez', 'prez', ), 
                            ], 
                        default= 'member',
                           )
    content = TextAreaField('', validators=[DataRequired()], default="note")
    
    submit = SubmitField('submit')
    
 
 