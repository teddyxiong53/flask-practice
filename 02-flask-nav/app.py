from flask import Flask, render_template
from flask_nav import Nav
from flask_nav.elements import Navbar, View, Subgroup, Link, Text, Separator
from flask_bootstrap import Bootstrap
from nav import nav, ExtendedNavbar, init_custom_nav_renderer

def top_nav():
    return ExtendedNavbar(
    title=View('hanliang', 'index'),
    root_class = 'navbar navbar-inverse',
    items = (
        View('aa', 'index'),
        View('bb', 'about'),
        Subgroup(
            'Product',
            View('cc', 'products', product='cc'),
            Separator(),
            Text("hhhhhhh"),
            View('dd', 'products', product='dd')
        ),
        Link('tech support', dest='http://www.baidu.com'),
    ),
    right_items=(
            View('Signup', 'index'),
    )
)
# 下面这个top，是id。
# 在html里，会通过nav.top这样来引用到这个变量。
nav.register_element('top', top_nav)

app = Flask(__name__)
Bootstrap(app)

nav.init_app(app)
init_custom_nav_renderer(app)
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')
@app.get('/about-us')
def about():
    return "about"

@app.get('/products/<product>')
def products(product):
    return str(product)

app.run(host='0.0.0.0', debug=True)

