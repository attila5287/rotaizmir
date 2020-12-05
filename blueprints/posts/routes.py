import random
from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from blueprints import db
from blueprints.models import Post, User
from blueprints.posts.forms import PostForm

posts = Blueprint('posts', __name__)

 
@posts.context_processor
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


@posts.context_processor
def inject_icons():
    pass
    def icons(label):
        pass
        gallery = { #font awesome icons for member forms
            "title": "s fa-highlighter", 
            "email": "s fa-envelope", 
            "id": "s fa-id-card", 
            "img_url": "s fa-image", 
            "is_admin": "s fa-user-md", 
            "is_prez": "s fa-user-md", 
            }
        
        return gallery.get(label, 's fa-edit')
    
    return dict(icons=icons)

@posts.route("/post/new", methods=['GET', 'POST'])
@posts.route("/post/new/", methods=['GET', 'POST'])
@posts.route("/post/new/<string:theme>", methods=['GET', 'POST'])
@posts.route("/post/new/<string:theme>/", methods=['GET', 'POST'])
def new_post(theme=''):
    user = current_user if current_user.is_authenticated else User.query.get_or_404(1)
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author=user)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_post.html',
                           theme=theme,
                           user=user,
                           form=form,
                           info_notes=[
                               'Public message board, user-created messages need to be approved by an admin.',
                           ],
                           access=[
                               'u',
                               'm',
                               'a',
                               'p',
                           ],
                           js=None,
                           legend='New Post Form',
                           title='New Post',

                           )

@posts.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@posts.route("/post/<int:post_id>/update/", methods=['GET', 'POST'])
@posts.route("/post/<int:post_id>/update/<string:theme>", methods=['GET', 'POST'])
@posts.route("/post/<int:post_id>/update/<string:theme>/", methods=['GET', 'POST'])
@login_required
def update_post(post_id,theme='no_change'):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('posts.post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('create_post.html', 
                           theme=theme,
                           title='Update Post',
                           form=form, 
                           legend='Update Post'
                           )


@posts.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('main.home'))

@posts.route("/post/<int:post_id>")
@posts.route("/post/<int:post_id>/")
def post(post_id=1, theme='no_change'):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', 
                           theme=theme, 
                           post=post, 
                           info_notes=[
                               'Shows the selected post individually. ',
                               'Update if posted by the current user.',
                           ],
                           access=[
                               'u',
                               'm',
                               'a',
                               'p',
                           ],
                           js=None,
                           legend='View Post',
                           title=post.title, 

                           )
