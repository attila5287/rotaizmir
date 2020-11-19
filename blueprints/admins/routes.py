import requests
from flask import (
  render_template, url_for, flash,
  redirect, request, abort, Blueprint,
  jsonify
)
from flask_login import (
  login_user, current_user, logout_user, login_required)
from blueprints import db
from blueprints.models import Member, User, Note, Request
from blueprints.admins.forms import UserMenu, TableModeSelect
from blueprints.members.forms import MemberMenu

admins = Blueprint('admins', __name__)

@admins.context_processor
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
    }

    return gallery.get(label, 's fa-edit')

  return dict(icons=icons)


@admins.route('/a/t/u', methods= [ 'GET', 'POST'])
@admins.route('/a/t/u/', methods= [ 'GET', 'POST'])
@admins.route('/admin/tables/users', methods= [ 'GET', 'POST'])
@admins.route('/admin/tables/users/', methods= [ 'GET', 'POST'])
def users_table():
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
    
  p_users = User.query.order_by(
    User.id.desc()).paginate(page=page, per_page=20, error_out=False)

  # these are pagination objects not all records on db
  # per page 20 instead
  table =  [
    {
      c.name:
      getattr(user, c.name)
      for c in user.__table__.columns}

    for user in p_users.items
    ]
  
  user_requests = {
    'for_member' : [1,  3,4,], 
    'for_admin'  : [  2,3,4,], 
    'for_prez'   : [1,  3,4,], 
  }
  
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
      'Admin dashboard, approve membership request from users or make a user admin.',
    ],
    access=[
      'a',
      'p',
    ],
    js=None,
    title='AdminTablesUser',
    legend='Admin Tables User',
    user_requests = user_requests,
    )

@admins.route('/a/t/m', methods= [ 'GET', 'POST'])
@admins.route('/a/t/m/', methods= [ 'GET', 'POST'])
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
      for c in member.__table__.columns
      }
    for member in p_members.items
    ]
  headers = [
    'id',
    'first_name',
    'middle_name',
    'last_name',
    'phone_num',
    'email',
    'gender',
    'is_prez',
    'is_admin',
    'user_id',
    'img_url',
    'linkedin',
    'twitter',
    'instagram',
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
              'Admin dashboard, tables to see all members, ',
            ],
            access=[
              'a',
              'p',
            ],
            js=None,
            title='AdminTablesMember',
            legend='Admin Tables Member',
            headers=headers,
            )

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

@admins.route('/membership/cancelled/<int:id>', methods= [ 'GET', 'POST'])
@admins.route('/membership/cancelled/<int:id>/', methods= [ 'GET', 'POST'])
def cancel_member(id):
  pass
  user = User.query.get_or_404(id)
  if user.is_member == 'n':
    pass
    return jsonify(
      {
             'status':'action not necessary',
             'user ID #{}'.format(id):'not a member',
             }
      )
  else:
    pass
    user.is_member = 'n'
    db.session.commit()
    return redirect(url_for('admins.users_table'))
    # return jsonify({'status': success_msg})

@admins.route('/admin/approved/<int:id>', methods= [ 'GET', 'POST'])
@admins.route('/admin/approved/<int:id>/', methods= [ 'GET', 'POST'])
def approve_admin(id):
  pass
  user = User.query.get_or_404(id)
  if not user.is_admin != 'y':
    pass
    return jsonify(
      {'status':'action not necessary',
       'user ID #{}'.format(id):'already a admin',
       }
    )
  else:
    pass
    user.is_admin = 'y'
    db.session.commit()
    return redirect(url_for('admins.users_table'))
    # return jsonify({'status': success_msg})

@admins.route('/admin/cancelled/<int:id>', methods= [ 'GET', 'POST'])
@admins.route('/admin/cancelled/<int:id>/', methods= [ 'GET', 'POST'])
def cancel_admin(id):
  pass
  user = User.query.get_or_404(id)
  if not user.is_admin != 'n':
    pass
    return jsonify(
      {
             'status':'action not necessary',
             'user ID #{}'.format(id):'not an admin',
             }
      )
  else:
    pass
    user.is_admin = 'n'
    db.session.commit()
    return redirect(url_for('admins.users_table'))

@admins.route('/prez/approved/<int:id>', methods= [ 'GET', 'POST'])
@admins.route('/prez/approved/<int:id>/', methods= [ 'GET', 'POST'])
def approve_prez(id):
  pass
  user = User.query.get_or_404(id)
  if not user.is_prez != 'y':
    pass
    return jsonify(
      {'status':'action not necessary',
       'user ID #{}'.format(id):'already a admin',
       }
    )
  else:
    pass
    user.is_prez = 'y'
    db.session.commit()
    return redirect(url_for('admins.users_table'))
    # return jsonify({'status': success_msg})


@admins.route('/prez/cancelled/<int:id>', methods= [ 'GET', 'POST'])
@admins.route('/prez/cancelled/<int:id>/', methods= [ 'GET', 'POST'])
def cancel_prez(id):
  pass
  user = User.query.get_or_404(id)
  if not user.is_prez != 'n':
    pass
    return jsonify(
      {
             'status':'action not necessary',
             'user ID #{}'.format(id):'not an admin',
             }
      )
  else:
    pass
    user.prez = 'n'
    db.session.commit()
    return redirect(url_for('admins.users_table'))

@admins.route('/a/n', methods= [ 'GET', 'POST'])
@admins.route('/a/n/', methods= [ 'GET', 'POST'])
def all_notes():
  pass

  return  jsonify( {'all' : 'notes'})
