from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo

from webapp.user.models import User

class LoginForm(FlaskForm):
        username = StringField('Имя пользователя', validators=[DataRequired()], render_kw={"class": "form-control"})
        password = PasswordField('Пароль', validators=[DataRequired()], render_kw={"class": "form-control"})
        submit = SubmitField('Отправить', render_kw={"class": "btn btn-primary"})


class RegistrationForm(FlaskForm):
        username = StringField('Имя пользователя', validators=[DataRequired()], render_kw={"class": "form-control"})
        email = StringField('Электронная почта', validators=[DataRequired(), Email()], render_kw={"class": "form-control"})
        password = PasswordField('Пароль', validators=[DataRequired()], render_kw={"class": "form-control"})
        password1 = PasswordField('Подтверждение пароля', validators=[DataRequired(), EqualTo("password")], render_kw={"class": "form-control"})
        submit = SubmitField('Отправить', render_kw={"class": "btn btn-primary"})

        def validate_username(self, username):
                user_count = User.query.filter_by(username=username.data).count()
                if user_count > 0:
                        raise ValidationError('Пользователь с таким именем уже существует')

        def validate_email(self, email):
                email_count = User.query.filter_by(email=email.data).count()
                if email_count > 0:
                        raise ValidationError('Пользователь с такой почтой уже существует')