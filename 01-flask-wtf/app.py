from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from flask import Flask, g, render_template, redirect, url_for
from flask_wtf.file import FileField, FileRequired
from werkzeug.utils import secure_filename
import os

class MyForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
WTF_CSRF_SECRET_KEY = 'a random string'

app = Flask(__name__)
app.config.from_object(__name__)
app.secret_key = "super secret key"
@app.route('/', methods=['GET', 'POST'])
def index():
    form = MyForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('index.html', form=form)
@app.route('/success')
def success():
    return 'success'

class PhotoForm(FlaskForm):
    photo = FileField(validators=[FileRequired()])

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    form = PhotoForm()
    if form.validate_on_submit():
        f = form.photo.data
        filename = secure_filename(f.filename)
        f.save(os.path.join('photos', filename))
        return redirect(url_for('index'))
    return render_template('upload.html', form=form)

app.run(host='0.0.0.0', debug=True)