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

@admins.route('/adm1ns')
def dashbo4rd():
    pass
    return render_template('dashboard.html')



@admins.route('/admins', methods= [ 'POST', 'GET'])
# @login_required
def dashboard():
    pass
    select_table = TableModeSelect()
    select_user = UserMenu()
    select_member = MemberMenu()
    all_members = [u for u in Member.query.all()]
    all_users = [u for u in User.query.all()]
    select_table.mode.choices = [
        (0, 'Show Members'), 
        (1, 'Show Users'), 
        (2, 'Show Admins'),        
    ]
    c =select_table.mode.choices
    opt = [
        label for (index,label) in c
    ]
    modes = dict(enumerate(opt))
    # return jsonify(modes)
        
    default_mode = modes[0]
    select_user.menu.choices = [
        (u.id, '{} | {}'.format(u.username.lower(), u.email).strip()) for u in all_users
    ]
    select_member.menu.choices = [
        ( m.id, '{}, {} | {}'.format(m.last_name.upper(), str(m.first_name+ ' ' + m.middle_name).title(), m.email).strip()) for m in all_members
    ]
    
    page = request.args.get('page', 1, type=int)
    
    p_users = User.query.order_by(
        User.id.desc()).paginate(page=page, per_page=20)
    p_members = Member.query.order_by(
        Member.id.desc()).paginate(page=page, per_page=20)

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
    #these are pagination objects not all on db
    table =  {
        modes[0] : [
            {
                c.name:
                getattr(member, c.name)
                for c in member.__table__.columns}

            for member in p_members.items
        ], 
        modes[1] : [
        {
            c.name:
            getattr(user, c.name)
            for c in user.__table__.columns}

        for user in p_users.items
        ],        
        modes[2] : [],
            
    }
    # return jsonify(table)
    
        
    if request.method == 'POST':    
        pass
        new_index = request.form['mode']
        selected_mode = modes[int(new_index)]
        
        return render_template('dashboard.html',
                            select_table=select_table,
                            select_user=select_user,
                            select_member=select_member,
                            members=p_members, 
                            headers=headers, 
                            table=table[selected_mode],
                            table_mode= selected_mode,
                            )
    
    return render_template('dashboard.html',
                           select_table=select_table,
                           select_user=select_user,
                           select_member=select_member,
                           members=p_members, 
                           headers=headers, 
                           table=table[default_mode],
                           table_mode= default_mode,
                           )

