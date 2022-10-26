from app.models import Book
from flask_wtf import FlaskForm
from wtforms.fields import (StringField, 
                            PasswordField, 
                            BooleanField, 
                            SubmitField, 
                            EmailField, 
                            SelectField
)
from wtforms.validators import Length, Email, DataRequired

class LoginForm(FlaskForm):
    email = EmailField("Email", validators=[
        Email("E-mail inválido")
    ])
    password = PasswordField("Senha", validators=[
        Length(3, 6, "O campo deve conter entre 3 a 6 caracteres.")
    ])
    remember = BooleanField("Permanecer Conectado")
    submit = SubmitField("Logar")

class RegisterForm(FlaskForm):
    name = StringField("Nome Completo", validators=[
        DataRequired("O campo é obrigatório.")
    ])
    email = EmailField("Email", validators=[
        Email("E-mail inválido")
    ])
    password = PasswordField("Senha", validators=[
        Length(3, 6, "O campo deve conter entre 3 a 6 caracteres.")
    ])

    submit = SubmitField("Cadastrar")

class BookForm(FlaskForm):
    name = StringField("Nome do livro", validators=[
        DataRequired("O campo é obrigatório")
    ])
    submit = SubmitField("Salvar")

class UserBookForm(FlaskForm):
    book = SelectField("Livro",coerce=int)
    submit = SubmitField("Salvar")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.book.choices = [
            (book.id, book.name) for book in Book.query.all()
        ]