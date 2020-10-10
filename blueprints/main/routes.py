from flask import render_template, request, Blueprint
from blueprints.models import Post

main = Blueprint('main', __name__)

# Drops all records, need to register again:DONT USE UNLESS NEW DB-MODEL-TABLE
# db.drop_all()
# Creates all tables, required if a new db-model to be tested

@main.route("/")
@main.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts)


@main.route("/about")
def about():
    return render_template('about.html', title='About')
