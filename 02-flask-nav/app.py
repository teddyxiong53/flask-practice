from flask import Flask, render_template
from flask_nav import Nav
from flask_nav.elements import *
from flask_bootstrap import Bootstrap
nav = Nav()

nav.register_element('top', Navbar(
    View('aa', 'index'),
    View('bb', 'about'),
    Subgroup(
        'Product',
        View('cc', 'products', product='cc'),
        Separator(),
        Text("hhhhhhh"),
        View('dd', 'products', product='dd')
    ),
    Link('tech support', dest='http://www.baidu.com')
))

app = Flask(__name__)
Bootstrap(app)

nav.init_app(app)

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
