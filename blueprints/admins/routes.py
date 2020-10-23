import requests
from flask import (
    render_template, url_for, flash,
    redirect, request, abort, Blueprint,
    jsonify
)
from flask_login import (
    login_user, current_user, logout_user, login_required)
from blueprints import db
from blueprints.models import Member, User
from blueprints.admins.forms import UserMenu
from blueprints.members.forms import MemberMenu

admins = Blueprint('admins', __name__)


@admins.route('/admins')
# @login_required
def dashboard():
    pass
    form_user = UserMenu()
    form_member = MemberMenu()
    all_members = [u for u in Member.query.all()]
    all_users = [u for u in User.query.all()]
    form_user.menu.choices = [
        (u.id, '{} | {}'.format(u.username.lower(), u.email).strip()) for u in all_users
    ]
    form_member.menu.choices = [
        ( m.id, '{}, {} | {}'.format(m.last_name.upper(), str(m.first_name+ ' ' + m.middle_name).title(), m.email).strip()) for m in all_members
    ]
    page = request.args.get('page', 1, type=int)
    members = Member.query.order_by(
        Member.id.desc()).paginate(page=page, per_page=24)

    columns = [c.name for c in Member.query.first().__table__.columns]
    icons = [
        's fa-id-card',
        's fa-asterisk',
        's fa-question-circle',
        's fa-asterisk',
        's fa-phone',
        's fa-envelope',
        's fa-venus-mars',
        's fa-stamp',
        's fa-user-md',
        's fa-user',
        's fa-image',
        'b fa-linkedin',
        'b fa-twitter',
        'b fa-instagram',
    ]
    headers = zip(icons, columns)
    table = [
        {
            c.name:
            getattr(member, c.name)
            for c in member.__table__.columns}

        for member in members.items
    ]

    # return jsonify({'status': 'success'})
    return render_template('dashboard.html',
                           access=['a'],
                           info_notes=['welcome admin!'],
                           form_user=form_user,
                           form_member=form_member,
                           members=members, 
                           headers=headers, 
                           table=table,
                           tsection_title= 'm or u',
                           )

