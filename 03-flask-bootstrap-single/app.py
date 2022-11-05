from flask import Flask, render_template, flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm, RecaptchaField
from flask_wtf.file import FileField
from wtforms import StringField, HiddenField, ValidationError, RadioField,\
    BooleanField, SubmitField, IntegerField, FormField, validators
from wtforms.validators import DataRequired


# straight from the wtforms docs:
class TelephoneForm(FlaskForm):
    country_code = IntegerField('Country Code', [DataRequired()])
    area_code = IntegerField('Area Code/Exchange', [DataRequired()])
    number = StringField('Number')


class ExampleForm(FlaskForm):
    field1 = StringField('First Field', description='This is field one.')
    field2 = StringField('Second Field', description='This is field two.',
                       validators=[DataRequired()])
    hidden_field = HiddenField('You cannot see this', description='Nope')
    # recaptcha = RecaptchaField('A sample recaptcha field')
    radio_field = RadioField('This is a radio field', choices=[
        ('head_radio', 'Head radio'),
        ('radio_76fm', "Radio '76 FM"),
        ('lips_106', 'Lips 106'),
        ('wctr', 'WCTR'),
    ])
    checkbox_field = BooleanField('This is a checkbox',
                                  description='Checkboxes can be tricky.')

    # subforms
    mobile_phone = FormField(TelephoneForm)

    # you can change the label as well
    office_phone = FormField(TelephoneForm, label='Your office phone')

    ff = FileField('Sample upload')

    submit_button = SubmitField('Submit Form')


    def validate_hidden_field(form, field):
        raise ValidationError('Always wrong')


def create_app(configfile=None):
    app = Flask(__name__)
    Bootstrap(app)

    # in a real app, these should be configured through Flask-Appconfig
    app.config['SECRET_KEY'] = 'devkey'
    app.config['RECAPTCHA_PUBLIC_KEY'] = \
        '6Lfol9cSAAAAADAkodaYl9wvQCwBMr3qGR_PPHcw'

    @app.route('/', methods=('GET', 'POST'))
    def index():
        form = ExampleForm()
        form.validate_on_submit()  # to get error messages to the browser
        flash('critical message', 'critical')
        flash('error message', 'error')
        flash('warning message', 'warning')
        flash('info message', 'info')
        flash('debug message', 'debug')
        flash('different message', 'different')
        flash('uncategorized message')
        return render_template('index.html', form=form)

    return app

if __name__ == '__main__':
    create_app().run(host='0.0.0.0', debug=True)