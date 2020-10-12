from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from blueprints import db
# from blueprints.models import Post
# from blueprints.posts.forms import PostForm

posts = Blueprint('posts', __name__)

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
