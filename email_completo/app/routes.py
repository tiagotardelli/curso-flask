from datetime import timedelta

from app.auth import auth as auth_blueprint
from app.book import book as book_blueprint
from app.user import user as user_blueprint
from app.email import email as email_blueprint

def init_app(app):
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(book_blueprint)
    app.register_blueprint(user_blueprint)
    app.register_blueprint(email_blueprint)
