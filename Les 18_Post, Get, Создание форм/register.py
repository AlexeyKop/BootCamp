from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField, PasswordField
from wtforms.validators import DataRequired
# flask-login - этот модуль позволяет делать шифрование данных


class RegisterForm(FlaskForm):
    name = StringField('Имя:', validators=[DataRequired()])
    mail = EmailField("Почта: ", validators=[DataRequired()])
    password = PasswordField('Пароль: ', validators=[DataRequired()])
    submit = SubmitField("Отправить")