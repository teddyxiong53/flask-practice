from flask import Blueprint, render_template, flash, redirect, url_for
from flask_bootstrap import __version__ as FLASK_BOOTSTRAP_VERSION
from flask_nav.elements import Navbar, View, Subgroup, Link, Text, Separator
from markupsafe import escape

from forms import SignupForm
from nav import nav

frontend = Blueprint('frontend', __name__)

nav.register_element('frontend_top', Navbar(
    View('Flask-Bootstrap', '.index'),
    View('Home', '.index'),
    View('Forms Example', '.example_form'),
    Subgroup(
        'Docs',
        Link('Flask-Bootstrap', dest='https://www.baidu.com'),
        Link('Flask-AppConfig', dest='www.baidu.com'),
        Link('Flask-Debug', dest='www.baidu.com'),
        Separator(),
        Text('Bootstrap'),
        Link('Get started', dest='www.baidu.com')
    )
))

@frontend.route('/')
def index():
    return render_template('index.html')

@frontend.route('/example-form', methods=['GET', 'POST'])
def example_form():
    form = SignupForm()
    if form.validate_on_submit():
        flash('hello {}'.format(escape(form.name.data)))
        return redirect(url_for('.index'))
    return render_template('signup.html', form=form)
    
