# -*- coding: utf-8 -*-
from flask import Flask, request, redirect, render_template
from config import app_config, app_active
from admin.Admin import start_views
from controller.User import UserController
from controller.Product import ProductController

config = app_config[app_active]

from flask_sqlalchemy import SQLAlchemy

def create_app(config_name):
    app = Flask(__name__, template_folder='templates')
    
    app.secret_key = config.SECRET
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['FLASK_ADMIN_SWATCH'] = 'paper'
    db = SQLAlchemy(config.APP)
    start_views(app,db)
    
    db.init_app(app)
    
    @app.route('/login/')
    def login():
        return 'Aqui entrará a tela de login'
    
    @app.route('/login/', methods=['POST'])
    def login_post():
        user = UserController()
        email = request.form['email']
        password = request.form['password']
        result = user.login(email, password)
        if result:
            return redirect('/admin')
        else:
            return render_template('login.html', data={'status': 401, 'msg':'Dados de usuário incorretos', 'type': None})
    
    @app.route('/recovery-password/')
    def recovery_password():
        return 'Aqui entrará a tela de recuperar senha'  
    
    @app.route('/recovery-password/', methods=['POST'])
    def send_recovery_password():
        user = UserController()
        result = user.recovery(request.form['email'])
        if result:
            return render_template('recovery.html', data={'status': 200, 'msg':'E-mail de recuperação enviado com sucesso'})
        else:
            return render_template('recovery.html', data={'status': 401, 'msg':'Erro ao enviar e-mail de recuperação'})
    
    @app.route('/profile/<int:id>/action/<action>/')
    def profile(id, action):
        if action == 'action1':
            return 'Ação action1 usuário de ID %d' % id
        elif action == 'action2':
            return 'Ação action2 usuário de ID %d' % id
        elif action == 'action3':
            return 'Ação action3 usuário de ID %d' % id

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

    @app.route('/product', methods=['POST'])
    def save_products():
        product = ProductController()
        result = product.save_product(request.form)
        if result:
            message = "Inserido"
        else:
            message = "Não inserido"
        return message
    
    @app.route('/product', methods=['PUT'])
    def update_products():
        product = ProductController()
        result = product.update_product(request.form)
        if result:
            message = "Editado"
        else:
            message = "Não Editado"
        return message
    
    
    return app