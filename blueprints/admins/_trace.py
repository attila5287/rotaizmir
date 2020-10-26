    return render_template('login.html',
                           form=form,
                           css=[
                               ('theme', 'cerulean', ),
                               ('main', 'main', ),
                           ],
                           info_notes=[
                               'Please login with your email address and password. ',
                           ],
                           access=[
                               'u',
                               'm',
                               'a',
                               'p',
                           ],
                           js=None,
                           legend='Login Form',
                           title='Login',

                           )
