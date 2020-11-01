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
from blueprints.admins.forms import UserMenu, TableModeSelect
from blueprints.members.forms import MemberMenu

admins = Blueprint('admins', __name__)

@admins.route('/admin/tables/members', methods= [ 'GET', 'POST'])
@admins.route('/admin/tables/members/', methods= [ 'GET', 'POST'])
def members_table():
    pass
    page = request.args.get('page', 1, type=int)
    
    select_user = UserMenu()
    select_member = MemberMenu()
    all_members = [u for u in Member.query.all()]
    all_users = [u for u in User.query.all()]
    
    select_user.menu.choices = [
        (u.id, '{} | {}'.format(u.username.lower(), u.email).strip()) for u in all_users
    ]
    select_member.menu.choices = [
        ( m.id, '{}, {} | {}'.format(m.last_name.upper(), str(m.first_name+ ' ' + m.middle_name).title(), m.email).strip()) for m in all_members
    ]        
    
    p_members = Member.query.order_by(
        Member.id.desc()).paginate(page=page, per_page=20, error_out=False)

    #these are pagination objects not all records on db
     #per page 20 instead
    table =  [
        {
            c.name:
            getattr(member, c.name)
            for c in member.__table__.columns}

        for member in p_members.items
        ]
    
    return render_template(
        'adm_tbl_memb.html',
                        select_user=select_user,
                        select_member=select_member,
                        members=p_members, 
                        table=table,
                        css=[('theme', '/minty/bootstrap', ),
                            ('main', 'main', ),
                            # ('custom', 'dashboard', ),
                        ],
                        info_notes=[
                            'Admin dashboard, approve membership request from members, ',
                        ],
                        access=[
                            'a',
                            'p',
                        ],
                        js=None,
                        title='AdminTablesMember',
                        legend='Admin Tables Member',
                        )




@admins.route('/admin/tables/users', methods= [ 'GET', 'POST'])
@admins.route('/admin/tables/users/', methods= [ 'GET', 'POST'])
def users_table():
    pass
    page = request.args.get('page', 1, type=int)
    
    select_table = TableModeSelect()
    select_user = UserMenu()
    select_member = MemberMenu()
    all_members = [u for u in Member.query.all()]
    all_users = [u for u in User.query.all()]
    
    select_user.menu.choices = [
        (u.id, '{} | {}'.format(u.username.lower(), u.email).strip()) for u in all_users
    ]
    select_member.menu.choices = [
        ( m.id, '{}, {} | {}'.format(m.last_name.upper(), str(m.first_name+ ' ' + m.middle_name).title(), m.email).strip()) for m in all_members
    ]        
    
    p_users = User.query.order_by(
        User.id.desc()).paginate(page=page, per_page=20, error_out=False)

    #these are pagination objects not all records on db
     #per page 20 instead
    table =  [
        {
            c.name:
            getattr(user, c.name)
            for c in user.__table__.columns}

        for user in p_users.items
        ]
    
    return render_template(
        'adm_tbl_usr.html',
                        select_user=select_user,
                        select_member=select_member,
                        users=p_users, 
                        table=table,
                        css=[('theme', '/minty/bootstrap', ),
                            ('main', 'main', ),
                            ('custom', 'dashboard', ),
                        ],
                        info_notes=[
                            'Admin dashboard, approve membership request from users, ',
                        ],
                        access=[
                            'a',
                            'p',
                        ],
                        js=None,
                        title='AdminTablesUser',
                        legend='Admin Tables User',
                        )


@admins.route('/make/admin/<int:id>', methods= [ 'GET', 'POST'])
@admins.route('/make/admin/<int:id>/', methods= [ 'GET', 'POST'])
def make_admin(id=1):
    pass
    user = User.query.get_or_404(id)
    user.is_admin = True
    return jsonify({'status' : 'success'})


@admins.route('/membership/approved/<int:id>', methods= [ 'GET', 'POST'])
@admins.route('/membership/approved/<int:id>/', methods= [ 'GET', 'POST'])
def approve_member(id):
    
    pass
    user = User.query.get_or_404(id)
    if user.is_member == 'y':
        pass
        return jsonify(
            {
             'status':'action not necessary',
             'user ID #{}'.format(id):'already a member',
             }
            )
    else:
        pass
        user.is_member = 'y'
    
        cast = [{
            c.name : getattr(user, c.name)
        } for c in user.__table__.columns]
        res={}
        for d in cast:
            for k,v in d.items():
                res[k] = v
        success_msg = 'user account {} is now a member'.format(res['username'])
        db.session.commit()
        return redirect(url_for('admins.users_table'))
        # return jsonify({'status': success_msg})


@admins.route('/link/user/<int:user_id>/<int:member_id>', methods= [ 'GET', 'POST'])
@admins.route('/link/user/<int:user_id>/<int:member_id>/', methods= [ 'GET', 'POST'])
def link_user(user_id, member_id):
    pass
    success_msg = 'user account #{} is now linked to member profile #{}'.format(user_id, member_id)
    return jsonify({'status':success_msg})
