from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore,\
        UserMixin, RoleMixin, login_required

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = '123'
app.config['SQLALCHEMY_DATABASE_URI']  = 'sqlite:///test.sqlite'
app.config['SECURITY_PASSWORD_SALT'] = 'MY_SALT'
db = SQLAlchemy(app)

roles_users = db.Table('roles_users', 
    db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
    db.Column('role_id', db.Integer(), db.ForeignKey('role.id')),
)

class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    comfirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users, 
        backref=db.backref('users', lazy='dynamic'))

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

@app.before_first_request
def create_user():
    db.create_all()
    # user_datastore.create_user(email='1073167306@qq.com', password='123456')
    db.session.commit()

@app.route('/', methods=['GET'])
@login_required
def home():
    return render_template('index.html')

app.run(host='0.0.0.0', debug=True)
