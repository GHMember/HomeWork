# Настройка полей форм 

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length
from app.models import User

# настройка полей формы входа 
class LoginForm(FlaskForm):
	username = StringField('Логин', validators=[DataRequired()])
	password = PasswordField('Пароль', validators=[DataRequired()])
	remember_me = BooleanField('Запомнить меня')
	submit = SubmitField('Войти')

# настройка полей формы регистрации 
class RegistrationForm(FlaskForm):
	username = StringField('Логин', validators=[DataRequired()])
	email = StringField('Электронная почта', validators=[DataRequired(), Email()])
	password = PasswordField('Пароль', validators=[DataRequired()])
	password2 = PasswordField('Повторите пароль', validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Зарегистрироваться')
	
	def validate_username(self, username):
		user = User.query.filter_by(username=username.data).first()
		if user is not None:
			raise ValidationError('Этот логин занят')
	
	def validate_email(self, email):
		user = User.query.filter_by(email=email.data).first()
		if user is not None:
			raise ValidationError('Такой адрес уже зарегистрирован')

# настройка полей формы редактирования профиля пользователя
class EditProfileForm(FlaskForm):
	username = StringField('Логин', validators=[DataRequired()])
	about_me = TextAreaField('Обо мне', validators=[Length(min=0, max=140)])
	submit = SubmitField('Сохранить')
	
	def __init__(self, original_username, *args, **kwargs):
		super(EditProfileForm, self).__init__(*args, **kwargs)
		self.original_username = original_username
	
	def validate_username(self, username):
		if username.data != self.original_username:
			user = User.query.filter_by(username=self.username.data).first()
			if user is not None:
				raise ValidationError('Такой логин уже зарегистрирован, выберите другой')

# настройка формы отправки сообщения от пользоваталя	
class PostForm(FlaskForm):
	post = TextAreaField('Сказать что-то', validators=[DataRequired(), Length(min=1, max=140)])
	submit = SubmitField('Отправить')