
from flask_login import LoginManager, UserMixin, login_user
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from flask import Flask, g, render_template, redirect, url_for, request
import flask_login

app  = Flask(__name__)
app.secret_key = '123'

login_manager = LoginManager()
login_manager.init_app(app)

class User(UserMixin):
    pass

class LoginForm(FlaskForm):
    username = StringField()
    password = StringField()

@login_manager.user_loader
def load_user(username):
    print("load user is called")
    user = User()
    user.id = username
    return user

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if request.form['username'] == 'admin' and request.form['password'] == 'admin':
            user = User()
            user.id = request.form['username']
            user.password = request.form['password']
            login_user(user)
            return redirect(url_for('protected'))
        else:
            return redirect(url_for('login'))
    return render_template('login.html', form=form)

@app.route('/protected')
@flask_login.login_required
def protected():
    return 'login as ' + flask_login.current_user.id

app.run(debug=True)
