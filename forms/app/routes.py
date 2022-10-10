from datetime import timedelta
import imp
from decouple import config

from app import db
from app.models import User, Book
from app.forms import LoginForm, RegisterForm, BookForm, UserBookForm

from flask import render_template, redirect, url_for, request, flash
from flask_login import (LoginManager, 
                         UserMixin, 
                         login_required, 
                         login_user, 
                         logout_user,
                         current_user
)
from werkzeug.security import generate_password_hash, check_password_hash



def init_app(app):
    @app.route("/")
    def index():
        users = User.query.all() # Select * from users;
        return render_template("users.html", users=users)

    @app.route("/user/<int:id>")
    @login_required
    def unique(id):
        user = User.query.get(id)
        return render_template("user.html", user=user)

    @app.route("/user/delete/<int:id>")
    def delete(id):
        user = User.query.filter_by(id=id).first()
        db.session.delete(user)
        db.session.commit()        

        return render_template("delete.html")

    @app.route("/register",methods=["GET", "POST"])
    def register():

        form = RegisterForm()

        if form.validate_on_submit():
            user = User(name = form.name.data,
                        email = form.email.data,
                        password = generate_password_hash(form.password.data)
            )

            db.session.add(user)
            db.session.commit()
            return redirect(url_for("index"))
        return render_template("register.html", form=form)

    @app.route("/login", methods=["GET", "POST"])
    def login():

        form = LoginForm()

        if form.validate_on_submit():

            user = User.query.filter_by(email=form.email.data).first()

            if not user:
                flash("Credências inválidas", "danger")
                return redirect(url_for("login"))

            if not check_password_hash(user.password, form.password.data):
                flash("Credências inválidas", "danger")
                return redirect(url_for("login"))

            login_user(user, remember=form.remember.data, duration=timedelta(days=7))
            return redirect(url_for("index"))

        return render_template("login.html", form=form)

    @app.route("/logout")
    @login_required
    def logout():
        logout_user()
        return redirect(url_for("index"))

    @app.route("/book/add", methods=["GET", "POST"])
    def book_add():
        form = BookForm()

        if form.validate_on_submit():
            book = Book(name = form.name.data)
            db.session.add(book)
            db.session.commit()

            flash("Livro cadastrado com sucesso!", "success")
            return redirect(url_for("book_add"))
        return render_template("book/add.html", form=form)
    

    @app.route("/user/<id>/add-book", methods=["GET", "SET"])
    def user_add_book(id):
        form = UserBookForm()

        if form.validate_on_submit():
            book = Book.query.get(form.book.data)
            current_user.books.append(book)
            db.session.add(current_user)
            db.session.commit()

            flash("Livro cadastrado com sucesso!", "success")
            return redirect(url_for("user_add_book", id=current_user.id))

        return render_template("book/user_add_book.html", form=form)
