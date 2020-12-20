import random
from flask import render_template, request, Blueprint
from blueprints.models import Post

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/about")
@main.route("/about/")
@main.route("/about/<string:theme>")
@main.route("/about/<string:theme>/")
def about(theme='minty'):
    pass
    return render_template(
        'about.html',
        theme=theme,
        info_notes=[
            'General instructions for guests',
        ],
        css=[
            ('theme', '/minty/bootstrap', ),
            ('main', 'main', ),
        ],
        js=[],
        legend='About App',
        title='About',
        access=[
            'u',
            'm',
            'a',
            'p',
        ],
    )

@main.route("/home")
@main.route("/home/")
@main.route("/home/<string:theme>")
@main.route("/home/<string:theme>/")
def home(theme='minty'):
    pass
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(
        Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', 
                           posts=posts,
                           theme=theme,
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
                           js=[],
                           legend='Public Posts',
                           title='Home | Public',
                           )


@main.context_processor
def inject_random_theme():
  pass
  def random_theme():
    pass
    list_of_themes = [
      'cerulean',
      'cyborg',
      'darkly',
      'lumen',
      'minty',
      'pulse',
      'slate',
      'solar',
      'spacelab',
      'superhero',
      'united',
    ]
    
    selected  = random.choice(list_of_themes)
    print(selected)
    return selected if selected else 'minty'

  return dict(random_theme=random_theme())


@main.route("/fa/icons")
@main.route("/fa/icons/")
@main.route("/fa/icons/<string:theme>")
@main.route("/fa/icons/<string:theme>/")
def fa_icons(theme=''):
    pass
    return render_template('fa_icons.html', 
                           theme=theme,
                           info_notes=[
                               'icons that actually-work!', 
                               'click on icon to copy tag or hover to see cls', 
                           ],
                           access=[
                               'u',
                               'm',
                               'a',
                               'p',
                           ],
                           legend='font awesome',
                           title='fa-icons',
                           )
