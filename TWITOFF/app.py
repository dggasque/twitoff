"""Code for our app"""

from decouple import config
from flask import Flask, render_template, request
from .models import DB, User


# make our app factory
def create_app():
    app = Flask(__name__)

    # add config for database
    app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE_URL')

    # 
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False   
    
    # have the database know about app
    DB.init_app(app)

    @app.route('/')
    def root():
        users = User.query.all()
        return render_template('base.html', title='Home', users=users)
    
    @app.route('/reset')
    def reset():
        DB.drop_all()
        DB.create_all()
        return render_template('base.html', title='Reset', users=[])

    return app 