from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')


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
