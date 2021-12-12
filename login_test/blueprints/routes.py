from flask import Blueprint
from flask import render_template
from flask_login import login_required


views = Blueprint(name='views', import_name=__name__)


@views.route('/')
@views.route('/index')
def index():
    return render_template('index.html', title='Welcome!')


@views.route('/secret')
@login_required
def secret():
    return 'secret area, have to be logged in!!'
