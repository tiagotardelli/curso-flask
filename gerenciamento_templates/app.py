from datetime import datetime
from flask import Flask, render_template, flash
from decouple import config
from filtros import formatdate

DICTONARY_USER = [{"name": "tiago tardelli",
                   "idade": 98,
                   "email": "t@t.com.br",
                   "active": True,
                   "since": datetime.utcnow()},
                 {"name": "moisés sasso",
                  "idade": 12,
                  "email": "f@g.com.br",
                  "active": False,
                  "since": datetime.utcnow()}
]

app = Flask(__name__,
            template_folder="tema",
            static_folder="public"
)
app.config["SECRET_KEY"] = config('SECRET_KEY')
app.jinja_env.filters["formatdate"] = formatdate


@app.route("/templates")
def templates():

    ##flash("Usuário criado com sucesso!")
    ##flash("Passei por aqui")

    user_page = True
    
    return render_template("index.html", user_page = user_page)

@app.route("/users")
def users():
   ## flash("Useres routes")

    users = DICTONARY_USER
    flash(message="users routes", category="success")
    return render_template("users.html", users = users)

if __name__ == "__main__":
    app.run(debug=True)
