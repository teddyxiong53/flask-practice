from flask import Flask
from flask_admin import Admin

app = Flask(__name__)
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'

admin = Admin(app, name='teddy', template_mode='bootstrap3')

app.run(host='0.0.0.0', debug=True)
