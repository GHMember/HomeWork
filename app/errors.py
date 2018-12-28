# Настройка обработки ошибок

from flask import render_template
from app import app, db

# настройка обработки ошибки 404 (обращение к несуществующей странице)
@app.errorhandler(404)
def not_found_error(error):
	return render_template('404.html'), 404

# настройка обработки ошибки 500 (внутрення ошибка сервера)	
@app.errorhandler(500)
def eternal_error(error):
	db.session.rollback()
	return render_template('500.html'), 500