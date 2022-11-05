from flask import Flask, render_template, flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm, RecaptchaField
from flask_wtf.file import FileField
from wtforms import StringField, HiddenField, ValidationError, RadioField,\
        BooleanField, SubmitField, IntegerField, FormField, validators
from wtforms.validators import DataRequired

from frontend import frontend
from nav import nav
SECRET_KEY = 'devkey'

app  = Flask(__name__)
app.config.from_object(__name__)
app.config['BOOTSTRAP_SERVE_LOCAL'] = True
Bootstrap(app)


app.register_blueprint(frontend)

nav.init_app(app)

app.run(host='0.0.0.0', debug=True)