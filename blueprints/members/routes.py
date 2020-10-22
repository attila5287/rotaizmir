import os
import csv
import codecs
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
from blueprints.members.forms import (
    MemberForm,
    CSVReaderForm,
    MemberEditForm
)
members = Blueprint('members', __name__)

@members.context_processor
def inject_icons():
    pass
    def icons(label):
        pass
        gallery = { #font awesome icons for member forms
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
            "user_id": "s fa-user-tag"
            }
        
        return gallery.get(label, 's fa-edit')
    
    return dict(icons=icons)


@members.route('/member/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    pass
    users = [u for u in User.query.all()]
    q_all = [Member.query.get_or_404(id)]
    members = [m for m in q_all]
    member = [m for m in q_all][0]
    d = [
        {
            c.name: getattr(member, c.name)
            for c in member.__table__.columns
        }
        for member in members
    ]
    form = MemberEditForm()
    
    if form.validate_on_submit():
        cast_into_dict = {field.name : field.data for field in form}
        cast_into_dict.pop('csrf_token', None)
        d = cast_into_dict.copy()
        for name, value in d.items():
            pass
            setattr(member, name, value) 
        db.session.commit()
        return redirect(url_for('members.show', id=member.id))
        # return jsonify(d)
    
    
    elif request.method == 'GET':
        form = MemberEditForm(**dict(enumerate(d))[0])
        form.user_id.choices = [
            (u.id, '{}|{}'.format(u.email, u.username)) for u in users
        ]        
        
    info = [
        'Edit member details',
    ]    
    access = [
        'a'
    ]
    
    return render_template('member_edit.html',
                           title="EditMember#{}".format(id),
                           legend="Edit Member #{}".format(id),
                           form = form,
                           member= member,
                           info= info,
                           access= access,
                           )

@members.route('/member/<int:id>')
def show(id):
    pass
    member = Member.query.get_or_404(id)
    access = [
        'a',
        'm',
    ]
    info = [
        'Members gallery'
    ]
    return render_template('member.html', m= member,
                           info=info,
                           access = access
                    
                           )


@members.route('/members/test', methods=['GET', 'POST'])
def tester():
    pass
    q_all = [Member.query.first_or_404()]

    members = [m for m in q_all]
    d = [
        {
            c.name: getattr(member, c.name)
            for c in member.__table__.columns
        }
        for member in members
    ]

    return jsonify(dict(enumerate(d))[0])


@members.route('/members/form', methods=['GET', 'POST'])
def add_member():
    pass
    form = MemberForm()
    if request.method == 'POST':
        rf = request.form

        cast = [
            {k: v
             for k, v in rf.items()
             }
        ][0]

        cast.pop('csrf_token', None)
        # return jsonify(cast)

        member = Member(**cast)
        db.session.add(member)
        db.session.commit()
        flash('Member added to database!', 'success')
        return redirect(url_for('members.home'))

    return render_template(
        'add_member.html',
        form=form,
        legend='Member Form',
        notes='add member via forms, one at a time!',
    )


@members.route('/members/file', methods=['GET', 'POST'])
def csv_feed():
    form = CSVReaderForm()
    if request.method == 'POST':
        csvfile = request.files['csv_file']
        reader = csv.DictReader(codecs.iterdecode(csvfile, 'windows-1252'))
        members = [
            Member(**row,
                   user_id=0,
                   is_admin='n',
                   is_prez='n',
                   instagram='',
                   twitter='',
                   linkedin='',
                   ) for row in reader
        ]
        # print(inventory).
        db.session.add_all(members)
        db.session.commit()
        flash('CSV read successfully!', 'success')
        return redirect(url_for('members.home'))
        # return render_template('about.html')

    return render_template(
        'csv_feed.html',
        title='CSV Feed',
        form=form,
    )


@members.route("/members/table")
def table():
    pass
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

    try:
        _ = [member for member in members.items]
    except:
        members = []

    return render_template('members_table.html', members=members, headers=headers, table=table)


@members.route("/members")
def home():
    pass
    page = request.args.get('page', 1, type=int)
    members = Member.query.order_by(
        Member.id.desc()).paginate(page=page, per_page=24)
    try:
        _ = [member for member in members.items]
    except:
        members = []

    return render_template('members.html', members=members)


@members.route("/members/api")
def api_all():
    pass
    q_all = Member.query.all()

    members = [m for m in q_all]
    d = [
        {
            c.name: getattr(member, c.name)
            for c in member.__table__.columns
        }
        for member in members
    ]

    return jsonify(dict(enumerate(d)))


@members.route("/members/db/init")
def db_init():
    pass  # UPLOAD ZILLOW HOUSE VALUE INDEX CSV'S MERGED
    existing_data = Member.query.first()

    if existing_data:
        pass
        return jsonify({
            'status0': 'database exists',
            'status1': 'db init is one time only',
            'status2': 'no upload necessary',
        })
    else:
        pass
        csv_url = 'https://gist.githubusercontent.com/attila5287/54a88147cbdfa6de88d5de0439250f3e/raw/55cadaafc200913578deddd4b43db5badc1dc0ce/members_ext.csv'

        with requests.get(csv_url, stream=True) as r:
            pass
            lines = (line.decode('utf-8') for line in r.iter_lines())
            csv_dict = [row for row in csv.DictReader(lines)]
            members = [
                Member(**row,
                       user_id=0,
                       ) for row in csv_dict
            ]
            # print(inventory).
            db.session.add_all(members)
            db.session.commit()

        return jsonify(csv_dict)
