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
from blueprints.models import Member
from blueprints.members.forms import (
    MemberForm, 
    CSVReaderForm
    )

members = Blueprint('members', __name__)
# inv_feed (doc: CSV read ex)
@members.route('/csv/feed', methods=['GET', 'POST'])
def csv_feed():
    form = CSVReaderForm()
    if request.method == 'POST':
        csvfile = request.files['csv_file']
        reader = csv.DictReader(codecs.iterdecode(csvfile, 'windows-1252'))
        members = [
            Member(**row, 
                    user_id= 0,
                    is_admin= 'n',
                    is_prez= 'n',
                    instagram= '',
                    twitter= '',
                    linkedin= '',
                    ) for row in reader
        ]
        # print(inventory).
        db.session.add_all(members)
        db.session.commit()
        flash('CSV read successfully!', 'success')
        return render_template('about.html')

    return render_template(
        'csv_feed.html',
        title='CSV Feed',
        form=form,
    )

    
@members.route("/members")
# @login_required()
def home():
    pass
    page = request.args.get('page', 1, type=int)
    members = Member.query.order_by(Member.id.desc()).paginate(page=page, per_page=24)
    try:
        _ = [ member for member in members.items ]
    except:
        members = []

    return render_template( 'members.html', members=members )

@members.route("/members/api")
def api_all():
   pass
   q_all = Member.query.all()
   
   members = [ m for m in q_all ]
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
        csv_url = 'https://gist.githubusercontent.com/attila5287/d80f78522096bf3b650b1f3bc7f65277/raw/6ee257198f35763d823d98a0955fbcef0cf2e941/members_demo.csv'

        with requests.get(csv_url, stream=True) as r:
            pass
            lines = (line.decode('utf-8') for line in r.iter_lines())
            csv_dict = [row for row in csv.DictReader(lines)]
            members = [
                Member(**row, 
                       user_id= 0,
                       is_admin= 'n',
                       is_prez= 'n',
                       instagram= '',
                       twitter= '',
                       linkedin= '',
                       ) for row in csv_dict
            ]
            # print(inventory).
            db.session.add_all(members)
            db.session.commit()

        return jsonify(csv_dict)

