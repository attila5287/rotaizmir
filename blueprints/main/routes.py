from flask import render_template, request, Blueprint
from blueprints.models import Post

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/about")
def about():
    pass

    return render_template('about.html',
                           info_notes=[
        'General instructions for guests',
    ],
        access=[
        'u',
        'm',
        'a',
        'p',
    ],
        css=[
        ('theme', '/minty/bootstrap', ),
        ('main', 'main', ),
    ],
        js=None,
        legend='About App',
        title='About'
    )


@ main.route("/home")
def home():
    pass
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(
        Post.date_posted.desc()).paginate(page=page, per_page=5)

    return render_template('home.html', posts=posts,
                           info_notes=[
                               'Follow public announcements, events.',
                           ],
                           access=[
                               'u',
                               'm',
                               'a',
                               'p',
                           ],
                           css=[
                               ('theme', '/minty/bootstrap', ),
                               ('main', 'main', ),
                           ],
                           js=None,
                           legend='Public Posts',
                           title='Home | Public',
                           )
