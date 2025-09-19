from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, PasswordField
from wtforms.validators import DataRequired

class UserInfoForm(FlaskForm):

    first_name = StringField('Primeiro nome', validators=[DataRequired()])
    last_name = StringField('Sobrenome', validators=[DataRequired()])
    institution = StringField('Instituição de ensino', validators=[DataRequired()])
    discipline = SelectField('Disciplina', choices=[
        ('Historia', 'História'),
        ('TI', 'T.I.'),
        ('Fisica', 'Física')
    ], validators=[DataRequired()])
    submit = SubmitField('Enviar')

class LoginForm(FlaskForm):

    username = StringField('Usuário ou E-mail', validators=[DataRequired()])
    password = PasswordField('Senha', validators=[DataRequired()])
    submit = SubmitField('Enviar')