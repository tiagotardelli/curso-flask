from datetime import timedelta
from flask import (
    render_template,
    url_for,
    redirect,
    flash
)
from app import db
from app.models import User, Book
from app.forms import LoginForm, RegisterForm, BookForm, UserBookForm
from . import auth
from flask import render_template, redirect, url_for, request, flash
from flask_login import (LoginManager, 
                         UserMixin, 
                         login_required, 
                         login_user, 
                         logout_user
)
from werkzeug.security import generate_password_hash, check_password_hash

@auth.route("/register",methods=["GET", "POST"])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        user = User(name = form.name.data,
                    email = form.email.data,
                    password = generate_password_hash(form.password.data)
        )

        db.session.add(user)
        db.session.commit()
        return redirect(url_for("user.index"))
    return render_template("register.html", form=form)

@auth.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        
        if not user:
            flash("Credências inválidas", "danger")
            return redirect(url_for(".login"))

        if not check_password_hash(user.password, form.password.data):
            flash("Credências inválidas", "danger")
            return redirect(url_for(".login"))

        login_user(user, remember=form.remember.data, duration=timedelta(days=7))
        return redirect(url_for("user.index"))

    return render_template("login.html", form=form)

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("user.index"))