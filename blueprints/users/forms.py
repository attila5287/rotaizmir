from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from blueprints.models import User


class RegistrationForm(FlaskForm):
    pass
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Requested username is not available, please choose another.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Requested email is not available, please choose another.')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=64)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    picture = FileField('Upload Profile Pic', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update username/email')


    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('Requested email is not available, please choose another.')
    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('Requested username is not available, please choose another.')

class RequestResetForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('There is no account with that email. You must register first.')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset Password')



class MemberRequestForm(FlaskForm):
    category = StringField('member',default='member')
    content = TextAreaField('content', validators=[DataRequired()])
    submit = SubmitField('request')
    
class AdminRequestForm(FlaskForm):
    category = StringField('admin',default='admin')
    content = TextAreaField('content', validators=[DataRequired()])
    submit = SubmitField('submit request')
    
class PrezRequestForm(FlaskForm):
    category = StringField('prez',default='prez')
    content = TextAreaField('content', validators=[DataRequired()])
    submit = SubmitField('submit request')
    
class PrezRequestForm(FlaskForm):
    content = TextAreaField('content', validators=[DataRequired()])
    submit = SubmitField('submit request')
    

