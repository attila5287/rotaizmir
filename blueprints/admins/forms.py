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
    category = SelectField(
                        choices=[
                            (0, 'default'), 
                            ], 
                        default= 0,
                           )
    content = TextAreaField('', validators=[DataRequired()])
    submit = SubmitField('submit')
