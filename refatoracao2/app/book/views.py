from . import book
from datetime import timedelta
from decouple import config
from . import book
from app import db
from app.models import User, Book
from app.forms import LoginForm, RegisterForm, BookForm, UserBookForm
from flask import render_template, redirect, url_for, request, flash
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from app.auth import auth as auth_blueprint

@book.route("/book/add", methods=["GET", "POST"])
def book_add():
    form = BookForm()

    if form.validate_on_submit():
        book = Book(name = form.name.data)
        db.session.add(book)
        db.session.commit()

        flash("Livro cadastrado com sucesso!", "success")
        return redirect(url_for(".book_add"))
    
    return render_template("book/add.html", form=form)
    
@book.route("/user/<id>/add-book", methods=["GET", "SET"])
def user_add_book(id):
    form = UserBookForm()

    if form.validate_on_submit():
        book = Book.query.get(form.book.data)
        current_user.books.append(book)
        db.session.add(current_user)
        db.session.commit()

        flash("Livro cadastrado com sucesso!", "success")
        return redirect(url_for(".user_add_book", id=current_user.id))

    return render_template("book/user_add_book.html", form=form)
