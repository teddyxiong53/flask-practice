from flask import Flask
from flask_admin import Admin, BaseView
import flask_admin
class MyAdminView(BaseView):
    @flask_admin.expose('/')
    def index(self):
        return self.render('myadmin.html')
class AnotherAdminView(BaseView):
    @flask_admin.expose('/')
    def index(self):
        return self.render('anotheradmin.html')

    @flask_admin.expose('/test/')
    def test(self):
        return self.render('test.html')

app = Flask(__name__, template_folder='templates')
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'

@app.route('/')
def index():
    return '<a href="/admin">click me to go to admin</a>'
admin = Admin(app, name='teddy', template_mode='bootstrap4')
admin.add_view(MyAdminView(name='view1', category='test'))
admin.add_view(AnotherAdminView(name='view2', category='test'))

# 这一行不能加了。因为上面已经构造admin的时候传递了app了。
# 否则会报重复定义的错误。
# admin.init_app(app)

app.run(host='0.0.0.0', debug=True)
