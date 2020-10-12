import csv
import requests
from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint, 
                   jsonify
                   )
from flask_login import current_user, login_required
from blueprints import db
from blueprints.models import Member
from blueprints.members.forms import MemberForm

members = Blueprint('members', __name__)

@members.route("/members/list")
def members_list():
   pass
   return jsonify({ 
                   'status' : 'success' ,
                   'members' : 'list' ,
                   })

@members.route("/db/init/members")
def db_init_members():
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
        csv_url = 'https://gist.githubusercontent.com/attila5287/d80f78522096bf3b650b1f3bc7f65277/raw/8c7402fb2206e67ba5b917f43c68859878cf6aad/members_demo.csv'

        with requests.get(csv_url, stream=True) as r:
            pass
            lines = (line.decode('utf-8') for line in r.iter_lines())
            csv_dict = [row for row in csv.DictReader(lines)]
            members = [
                Member(**row, 
                       user_id= 0,
                       is_admin= 'n',
                       is_prez= 'n',
                       ) for row in csv_dict
            ]
            # print(inventory).
            db.session.add_all(members)
            db.session.commit()

        return jsonify(csv_dict)
