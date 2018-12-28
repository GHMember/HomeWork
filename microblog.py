# Настройка оболочки приложения
from app import create_app, db, cli
from app.models import User, Post

app = create_app()
cli.register(app)

# настройка контекста оболочки, который добавляет экземпляр и модели базы данных в сеанс оболочки
@app.shell_context_processor
def make_shell_context():
	return {'db': db, 'User': User, 'Post': Post}