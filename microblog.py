# Настройка оболочки приложения
from app import app, db
from app.models import User, Post

# настройка контекста оболочки, который добавляет экземпляр и модели базы данных в сеанс оболочки
@app.shell_context_processor
def make_shell_context():
	return {'db': db, 'User': User, 'Post': Post}