from flask import render_template, request, Blueprint
from blueprints.models import Post

main = Blueprint('main', __name__)

@main.route("/home")
def home():
    pass
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)

    try:
        _ = [post for post in posts]
    except:
        posts = []


    return render_template('home.html', posts=posts)


@main.route("/")
@main.route("/about")
def about():
    pass

    return render_template('about.html', title='About')
