from flask import Flask, render_template, url_for, session, redirect, flash, request
from flask_bootstrap import Bootstrap
from forms import UserInfoForm, LoginForm
from wtforms.validators import DataRequired
from datetime import datetime

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'senhasecreta'

@app.route('/', methods=['GET', 'POST'])
def index():
    form = UserInfoForm()
    user_data = None 

    if form.validate_on_submit():
        addr_client = request.remote_addr
        host = request.host

        user_data = {
            'first_name': form.first_name.data,
            'last_name': form.last_name.data,
            'institution': form.institution.data,
            'discipline': form.discipline.data,
            'addr_client': addr_client,
            'host': host
        }
        form = UserInfoForm()

    local_time = datetime.now().strftime('%B %d, %Y %I:%M %p')

    return render_template('homepage.html', form=form, user_data=user_data, local_time=local_time)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return render_template('login_result.html', username=form.username.data)
        
    return render_template('login.html', form=form)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404error.html'), 404