# -*- coding: utf-8 -*-
from flask import Flask
# config import
from config import app_config, app_active
from flask_sqlalchemy import SQLAlchemy

config = app_config[app_active]

def create_app(config_name):
    app = Flask(__name__, template_folder='templates')
    app.secret_key = config.SECRET
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db = SQLAlchemy(config.APP)
    db.init_app(app)

    @app.route('/')
    def index():
        return 'Hello World!'
    
    @app.route('/login/')
    def login():
        return 'Aqui entrará a tela de login'
    
    @app.route('/recovery-password/')
    def recovery_password():
        return 'Aqui entrará a tela de recuperar senha'  
    
    @app.route('/profile/<int:id>/action/<action>/')
    def profile(id, action):
        if action == 'action1':
            return 'Ação action1 usuário de ID %d' % id
        elif action == 'action2':
            return 'Ação action2 usuário de ID %d' % id
        elif action == 'action3':
            return 'Ação action3 usuário de ID %d' % id
# O código da def profile já existe, continue a partir dele.
    @app.route('/profile', methods=['POST'])
    def create_profile():
        username = request.form['username']
        password = request.form['password']
        
        return 'Essa rota possui um método POST e criará um usuário com os dados de usuário %s e senha %s' % (username, password)

    @app.route('/profile/<int:id>', methods=['PUT'])
    def edit_total_profile(id):
        username = request.form['username']
        password = request.form['password']
        
        return 'Essa rota possui um método PUT e editará o nome do usuário para %s e a senha para %s' % (username, password)

    return app