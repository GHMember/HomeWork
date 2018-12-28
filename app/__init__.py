# Настройки представления реализации пакета

import logging
from logging.handlers import RotatingFileHandler
import os
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_view = 'auth.login'
login.login_message = ("Пожалуйста, войдите, чтобы открыть эту страницу.")
bootstrap = Bootstrap()

# настройка поведения приложения в случае если отключен режим отладки
def create_app(config_class=Config):
	
	app = Flask(__name__)
	app.config.from_object(config_class)
	db.init_app(app)
	migrate.init_app(app, db)
	login.init_app(app)	
	bootstrap.init_app(app)
	
	if not app.debug and not app.testing:
		
		if app.config['LOG_TO_STDOUT']:
			stream_handler = logging.StreamHandler()
			stream_handler.setLevel(logging.INFO)
			app.logger.addHandler(stream_handler)		
		else:
			if not os.path.exists('logs'):
				os.mkdir('logs')
			file_handler = RotatingFileHandler('logs/microblog.log', maxBytes=10240, backupCount=10)
			file_handler.setFormatter(logging.Formatter(
				'%(asctime)s %(levelname)s: %(message)s '
				'[in %(pathname)s:%(lineno)d]'))
			file_handler.setLevel(logging.INFO)
			app.logger.addHandler(file_handler)
		
		app.logger.setLevel(logging.INFO)
		app.logger.info('Microblog startup')
	
	return app
	
from app import models