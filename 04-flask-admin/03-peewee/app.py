import uuid
import peewee
from flask import Flask
import flask_admin as admin
from flask_admin import Admin
from flask_admin.contrib.peewee import ModelView

app = Flask(__name__)
app.config['SECRET_KEY']  = '123'

db = peewee.SqliteDatabase('test.sqlite')

class BaseModel(peewee.Model):
    class Meta:
        database = db

class User(BaseModel):
    username = peewee.CharField(max_length=80)
    email = peewee.CharField(max_length=120)

    def __str__(self) -> str:
        return self.username

class UserInfo(BaseModel):
    key = peewee.CharField(max_length=64)
    value = peewee.CharField(max_length=64)
    user = peewee.ForeignKeyField(User)

    def __str__(self) -> str:
        return f'{self.key}: {self.value}'

class Post(BaseModel):
    id = peewee.UUIDField(primary_key=True, default=uuid.uuid4)
    title = peewee.CharField(max_length=120)
    text = peewee.TextField(null=False)
    date = peewee.DateTimeField()
    
    user = peewee.ForeignKeyField(User)

    def __str__(self) -> str:
        return self.title

class UserAdmin(ModelView):
    inline_models = (UserInfo,)

class PostAdmin(ModelView):
    column_exclude_list = ['text']
    column_sortable_list = ('title', ('user', User.email), 'date')
    column_searchable_list = ('title', User.username)
    column_filters = ('title', 'date', User.username)

    form_ajax_refs = {
        'user': {
            'fields': (User.username, 'email')
        }
    }
@app.route('/')
def index():
    return '<a href="/admin/">to admin</a>'

admin = Admin(app, name='example:peewee')
admin.add_view(UserAdmin(User))
admin.add_view(PostAdmin(Post))

try:
    User.create_table()
    UserInfo.create_table()
    Post.create_table()
except:
    pass

app.run(host='0.0.0.0', debug=True)
