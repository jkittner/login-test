from flask import Blueprint
from flask import flash
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from flask_login import current_user
from flask_login import login_user
from flask_login import logout_user
from werkzeug.urls import url_parse

from login_test.forms import LoginForm
from login_test.models import User

auth = Blueprint(name='auth', import_name=__name__)


@auth.route('/login', methods=('GET', 'POST'))
def login():
    if current_user.is_authenticated:
        flash('logged in!')
        return redirect(url_for('views.index'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid Username or password')
            return redirect(url_for('auth.login'))

        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('views.index')

        return redirect(next_page)

    return render_template('login.html', title='Sign In', form=form)


@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('views.index'))
