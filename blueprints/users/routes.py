from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from blueprints import db, bcrypt
from blueprints.models import User, Post
from blueprints.users.forms import (
    RegistrationForm, LoginForm, UpdateAccountForm,RequestResetForm, ResetPasswordForm
)
from blueprints.users.utils import save_picture

users = Blueprint('users', __name__)



# function that takes /register user input thru reg-form
@users.route("/regist3r", methods=['GET', 'POST'])
def regist3r():
  pass
  hashed_password = bcrypt.generate_password_hash(
    request.form['password']).decode('utf-8')
  print('test pw')
  print(hashed_password)
  user = User(
    username=request.form['username'],
    email=request.form['email'],
    img_url= 0,
    password=hashed_password
  )
  db.session.add(user)
  db.session.commit()
  flash('Your account has been created! You are now able to log in', 'success')
  return redirect(url_for('users.login'))

@users.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('users.login'))
    return render_template('register.html', title='Register', form=form)


@users.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@users.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('main.home'))


@users.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('users.account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('account.html', title='Account',
                           image_file=image_file, form=form)


@users.route("/user/<string:username>")
def user_posts(username):
    page = request.args.get('page', 1, type=int)
    user = User.query.filter_by(username=username).first_or_404()
    posts = Post.query.filter_by(author=user)\
        .order_by(Post.date_posted.desc())\
        .paginate(page=page, per_page=5)
    return render_template('user_posts.html', posts=posts, user=user)

@users.route("/user/<int:user_1d>/delete", methods=['GET', 'POST'])
def delete_user_by_ID(user_1d):
    pass
    User.query.filter_by(id=user_1d).delete()
    db.session.commit()
    flash('Test user have been deleted!', 'success')
    return redirect(url_for('main.home'))

    