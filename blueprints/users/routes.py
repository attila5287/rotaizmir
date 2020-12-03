import sys
from datetime import datetime
import random
from random import shuffle
import csv
import requests
from flask import render_template, url_for, flash, redirect, request, Blueprint, jsonify
from flask_login import login_user, current_user, logout_user, login_required
from blueprints import db, bcrypt
from blueprints.models import User, Post, Nickname, Member, Color, Note
from blueprints.users.forms import (
    RegistrationForm, LoginForm, UpdateAccountForm, RequestResetForm, ResetPasswordForm) 
from blueprints.users.utils import save_picture, send_reset_email
from blueprints.users.forms import MemberRequestForm, AdminRequestForm, PrezRequestForm

users = Blueprint('users', __name__)
 
@users.context_processor
def inject_random_theme():
  pass
  def random_theme():
    pass
    list_of_themes = [
      'cerulean',
      'cyborg',
      'darkly',
      'lumen',
      'minty',
      'pulse',
      'slate',
      'solar',
      'spacelab',
      'superhero',
      'united',
    ]
    
    selected  = random.choice(list_of_themes)
    print(selected)
    return selected if selected else 'minty'

  return dict(random_theme=random_theme())

@users.context_processor
def inject_icons():
    pass
    def icons(label):
        pass
        gallery = {  # font awesome icons for member forms
            "email": "s fa-envelope",
            "first_name": "s fa-user-edit",
            "gender": "s fa-venus-mars",
            "id": "s fa-id-card",
            "img_url": "s fa-image",
            "instagram": "b fa-instagram",
            "is_admin": "s fa-user-md",
            "is_prez": "s fa-user-md",
            "last_name": "s fa-user-edit",
            "linkedin": "b fa-linkedin",
            "middle_name": "s fa-user-edit",
            "phone_num": "s fa-phone",
            "twitter": "b fa-twitter",
            "user_id": "s fa-user-tag",
            "menu": "s fa-sort",
            "picture": "s fa-image",
        }

        return gallery.get(label, 's fa-edit')

    return dict(icons=icons)

@users.route("/reg/post/public/<string:gen_username>", methods=['GET', 'POST'])
def reg_post_public(gen_username):
    pass  # function to run when new user registered btn hit
    user = User.query.filter_by(username=gen_username).first()
    if user:
        raise ValidationError(
            'That username is taken. Please choose a different one.')
    hashed_password = bcrypt.generate_password_hash(
        request.form["password"]).decode('utf-8')
    user = User(
        username=gen_username,
        email=request.form["email"],
        password=hashed_password,
        img_url=0,
        is_member='n',
        is_admin='n',
    )

    db.session.add(user)
    db.session.commit()
    flash('Your account has been created! You are now able to log in', 'success')
    return redirect(url_for('users.login'))

@users.route("/reg_post", methods=['POST'])
def reg_post():
    pass  # function to run when new user registered btn hit
    hashed_password = bcrypt.generate_password_hash(
        request.form["password"]).decode('utf-8')
    user = User(
        username=request.form["username"],
        email=request.form["email"],
        password=hashed_password,
        img_url=0,
        is_member='n',
        is_admin='n',
    )
    db.session.add(user)
    db.session.commit()
    flash('Your account has been created! You are now able to log in', 'success')
    return redirect(url_for('users.login'))

@users.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('main.home'))

@users.route("/set/profile/picture/<int:user_id>/<int:img_index>", methods=['GET', 'POST'])
@login_required
def set_profile_pic(user_id, img_index):
    pass
    current_user.img_url = img_index
    db.session.commit()
    return redirect(url_for('users.account'))

@users.route("/user/<int:id>")
@users.route("/user/<int:id>/")
def user_posts(id):
    pass
    page = request.args.get('page', 1, type=int)
    user = User.query.get_or_404(id)
    
    posts = Post.query.filter_by(author=user)\
        .order_by(Post.date_posted.desc())\
        .paginate(page=page, per_page=5)

    return render_template('user_posts.html', posts=posts, user=user)


@users.route("/reset_password", methods=['GET', 'POST'])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RequestResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        flash('An email has been sent with instructions to reset your password.', 'info')
        return redirect(url_for('users.login'))
    return render_template('reset_request.html', title='Reset Password', form=form)


@users.route("/reset_password/<token>", methods=['GET', 'POST'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    user = User.verify_reset_token(token)
    if user is None:
        flash('That is an invalid or expired token', 'warning')
        return redirect(url_for('users.reset_request'))

    form = ResetPasswordForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(
            form.password.data).decode('utf-8')
        user.password = hashed_password
        db.session.commit()
        flash('Your password has been updated! You are now able to log in', 'success')
        return redirect(url_for('users.login'))
    return render_template('reset_token.html', title='Reset Password', form=form)


@users.route("/db/init/nicknames")
def db_init_nicknames():
    pass  # UPLOAD ZILLOW HOUSE VALUE INDEX CSV'S MERGED
    existing_data = Nickname.query.first()

    if existing_data:
        pass
        return jsonify({
            'status0': 'database exists',
            'status1': 'db init is one time only',
            'status2': 'no upload necessary',
        })
    else:
        pass
        csv_url = 'https://gist.githubusercontent.com/attila5287/0e5e9c50c942fa916a3f95f3b5aff6db/raw/65e78a999102d31268e20fb7fc736d2160e6afbb/nicknames.csv'

        with requests.get(csv_url, stream=True) as r:
            pass
            lines = (line.decode('utf-8') for line in r.iter_lines())
            csv_dict = [row for row in csv.DictReader(lines)]
            nicknames = [
                Nickname(**row) for row in csv_dict
            ]
            # print(inventory)
            db.session.add_all(nicknames)
            db.session.commit()

        return jsonify(csv_dict)


@users.route('/nicknames/api')
def nicknames_api():
    pass
    q_db = Nickname.query.all()
    q_all = [  # query all
        n for n in q_db
    ]
    d = [q.nickname for q in q_all]
    random.shuffle(d)
    return jsonify(dict(enumerate(d)))


@users.route("/db/init/colors")
def db_init_colors():
    pass  # UPLOAD ZILLOW HOUSE VALUE INDEX CSV'S MERGED
    existing_data = Color.query.first()

    if existing_data:
        pass
        return jsonify({
            'status0': 'database exists',
            'status1': 'db init is one time only',
            'status2': 'no upload necessary',
        })
    else:
        pass
        csv_url = 'https://gist.githubusercontent.com/attila5287/3f0373400332073d5391abd4cf0665f3/raw/66791b84df3eded96f8bbea74115200da2f5055a/colors.csv'

        with requests.get(csv_url, stream=True) as r:
            pass
            lines = (line.decode('utf-8') for line in r.iter_lines())
            csv_dict = [row for row in csv.DictReader(lines)]
            colors = [
                Color(**row) for row in csv_dict
            ]
            # print(inventory)
            db.session.add_all(colors)
            db.session.commit()

        return jsonify(csv_dict)


@users.route('/colors/api')
def colors_api():
    pass
    q_db = Color.query.all()
    q_all = [  # query all
        c for c in q_db
    ]
    random.shuffle(q_all)

    indexed = [{c.name: getattr(q, c.name)
                for c in q.__table__.columns} for q in q_all]
    return jsonify(dict(enumerate(indexed)))


@users.route("/login", methods=['GET', 'POST'])
@users.route("/login/", methods=['GET', 'POST'])
@users.route("/login/<string:theme>", methods=['GET', 'POST'])
@users.route("/login/<string:theme>/", methods=['GET', 'POST'])
def login(theme='minty'):
    pass
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('users.account'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html',
                           theme=theme,
                           form=form,
                           css=[
                               ('theme', '/minty/bootstrap', ),
                               ('main', 'main', ),
                            #    ('custom', 'cards', ),
                           ],
                           info_notes=[
                               'Please login with your email address and password. ',
                           ],
                           access=[
                               'u',
                               'm',
                               'a',
                               'p',
                           ],
                           js=None,
                           legend='Login Form',
                           title='Login',

                           )

@users.route("/user/<int:id>")
def userposts_byid(id):
    page = request.args.get('page', 1, type=int)
    user = User.query.get_or_404(id)
    posts = Post.query.filter_by(author=user)\
        .order_by(Post.date_posted.desc())\
        .paginate(page=page, per_page=5)
    return render_template('user_posts.html', 
                           posts=posts, 
                           user=user, 
                           css=[
                               ('theme', '/minty/bootstrap', ),
                               ('main', 'main', ),
                           ],
                           info_notes=[
                               'Show all posts by the user #{}'.format(id),
                           ],
                           access=[
                               'u',
                               'm',
                               'a',
                               'p',
                           ],
                           js=None,
                           legend='Posts by {} ({})'.format(user.username, posts.total),
                           title='User#{} Posts'.format(id),
                           

                           )

# forms to register
@users.route("/register", methods=['GET', 'POST'])
@users.route("/register/", methods=['GET', 'POST'])
@users.route("/register/<string:theme>", methods=['GET', 'POST'])
@users.route("/register/<string:theme>/", methods=['GET', 'POST'])
def register(theme='minty'):
    form = RegistrationForm()
    
    if current_user.is_authenticated:
        return redirect(url_for('users.account'))

    # form.username.choices = Nickname.query.all()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(
            form.password.data).decode('utf-8')
        user = User(username=form.username.data,
                    email=form.email.data, 
                    password=hashed_password, 
                    img_url=0)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('users.login'))
    return render_template('register.html', 
                               theme=theme, 
                               form=form, 
                           legend='Register',
                            css=[
                                ('theme', '/minty/bootstrap', ),
                                ('main', 'main', ),
                            ],
                            info_notes=[
                                'Your email and password will be used for login',
                                'Choose your display name by random generators below',
                            ],
                            access=[
                                'u',
                                'm',
                                'a',
                                'p',
                            ],
                            js = [
                                ('register', 'nicknames', ),
                                ('register', 'colors', ),
                                ('register', 'numbers-countup', ),
                                ('plugins', 'count-up', ),
                                ('register', 'signup-as', ),
                                ],
                            title='SignUp',
                            

                            )

@users.route("/account", methods=['GET', 'POST'])
@users.route("/account/", methods=['GET', 'POST'])
@users.route("/account/<string:theme>", methods=['GET', 'POST'])
@users.route("/account/<string:theme>/", methods=['GET', 'POST'])
@login_required
def account(theme=''):
    pass
    form = UpdateAccountForm()
    
    formdata_posted = (request.method == 'POST')
    
    if formdata_posted and form.validate_on_submit():
        pass
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Username and/or Email updated!', 'success')
        return redirect(url_for('users.account'))

    elif request.method == 'GET':
        pass
        form.username.data = current_user.username
        form.email.data = current_user.email
    
    first_random = random.randint(0,69)
    return render_template('account.html',
                           theme = theme,
                           first_random = first_random,
                           form=form,
                           css=[ 
                               ('theme', '/minty/bootstrap', ),
                               ('main', 'main', ),
                           ],
                           info_notes=[
                               'On left is the current (temporary) picture,',
                               'Click (or Tap) suggested picture for next suggestion or hit the button to !',
                           ],
                           access=[
                               'u',
                               'm',
                               'a',
                               'p',
                           ],
                           js=[
                               ('users', 'account', ),
                           ],
                           legend='Edit User Account',
                           title='Account',
                           )

@users.route('/delete/request/<int:id>')
def delete_request(id):
    pass
    req = Note.query.get_or_404(id)
    db.session.delete(req)
    db.session.commit()
    return redirect(url_for('users.user_requests'))

@users.context_processor
def inject_icons():
  pass
  def icons(label):
    pass
    gallery = {  # font awesome icons for member forms
      "email": "s fa-envelope",
      "first_name": "s fa-user-edit",
      "gender": "s fa-venus-mars",
      "id": "s fa-id-card",
      "image_file": "s fa-file-image",
      "img_url": "s fa-image",
      "instagram": "b fa-instagram",
      "is_admin": "s fa-user-md",
      "is_member": "s fa-user-check",
      "is_prez": "s fa-user-shield",
      "last_name": "s fa-user-edit",
      "linkedin": "b fa-linkedin",
      "middle_name": "s fa-question-circle",
      "phone_num": "s fa-phone",
      "twitter": "b fa-twitter",
      "user_id": "s fa-user-tag",
      "menu": "s fa-sort",
      "new_note": "s fa-sticky-note",
      "display_requests": "b fa-tripadvisor",
      "make_admin": "s fa-user-md",
      "make_member": "s fa-user-check",
      "make_prez": "s fa-user-shield",
      "admin_request":  "s fa-concierge-bell",
      "member_request": "s fa-concierge-bell",
      "prez_request":   "s fa-concierge-bell",
      "delivered":   "s fa-envelope",
      "denied":   "s fa-gavel",
      "approved":   "s fa-stamp",
      "pending":  "s fa-balance-scale",
      "date_posted": "r fa-calendar-alt",
      "note_content": "r fa-paper-plane",
      "req_content": "r fa-file-alt",
      'member' : 's fa-user-check',
      'admin' : 's fa-user-md',
      'prez' : 's fa-user-graduate',
    }
    return gallery.get(label, 's fa-edit')

  return dict(icons=icons)

@users.context_processor
def inject_status_style():
  pass
  def styles(label):
    pass
    
    gallery = {  # font awesome icons for member forms
      "approved": "primary",
      "pending": "info",
      "denied": "secondary",
      "delivered": "warning",
      "received": "warning",
    }
    
    return gallery.get(label, '')

  return dict(styles=styles)

@users.context_processor
def inject_tooltip_titles():
  pass
  def tooltip_titles(status):
    pass
    mouseover_text = {  # tooltip for info
      "approved":  "request approved",
      "pending":   "request needs further review",
      "denied":    "request denied, read note carefully for details and send another request",
      "delivered": "user request to gain access to an authorization level",
      "received":  "user request to gain access to an authorization level",
    }
    
    return mouseover_text.get(status, '')

  return dict(tooltip_titles=tooltip_titles)


@users.route('/u/r', methods=['GET','POST'])
@users.route('/u/r/', methods=['GET','POST'])
@users.route('/user/requests/', methods=['GET','POST'])
@users.route('/user/requests/', methods=['GET','POST'])
@users.route('/u/r/<string:theme>', methods=['GET','POST'])
@users.route('/u/r/<string:theme>/', methods=['GET','POST'])
@users.route('/user/requests/<string:theme>', methods=['GET','POST'])
@users.route('/user/requests/<string:theme>/', methods=['GET','POST'])
@login_required
def user_requests(theme='minty'):
    pass
    # theme = theme if theme else 'minty'
    
    member_form = MemberRequestForm()
    admin_form = AdminRequestForm()
    prez_form = PrezRequestForm()
    active_requests = Note.query.filter_by(for_user=current_user).all()
    notes_for_user = Note.query.filter_by(for_user=current_user )
    cats = ['member','admin','prez',]
    d = {}
    for cat in cats:
      pass
      filtered = notes_for_user.filter_by(category=cat).all()
      d[cat] = filtered
      
    disp_reqs = {
      current_user.id : d
    }    
    
    # list of users that has active requests
    requestors = []
    
    # collects all categor
    for req in Note.query.filter_by(type='req').all():
        pass
        requestors.append(req.user_id)
        
    requestors = [
        r for  r in requestors
    ]      
    
    formdata_posted = (request.method == 'POST')
    if formdata_posted:
        pass
        usr_req = Note(
            type='req',
            category=request.form['category'],
            status='delivered',
            content=request.form['content'],
            user_id=current_user.id,
            )
        db.session.add(usr_req)
        db.session.commit()
        flash('User {} {} request delivered'.format(current_user.id, request.form['category'], ), 'success')    
        return redirect(url_for('users.user_requests'))        

    return render_template('user_reqs.html',
                           theme=theme,
                           requestors=requestors,
                           disp_reqs = disp_reqs,
                           member_form=member_form,
                           admin_form=admin_form,
                           prez_form=prez_form,
                           legend='User Requests',
                           info_notes = [
                             'Send requests for user account authorization',
                             'Check recently made requests',
                           ],
                           )

