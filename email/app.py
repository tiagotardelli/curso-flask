from socket import MsgFlag
from flask import Flask, render_template
from flask_mail import Mail, Message
from decouple import config


config= {     
   "MAIL_SERVER": config("MAIL_SERVER"),
   "MAIL_PORT": int(config("MAIL_PORT")),
   "MAIL_USE_TLS": bool(config("MAIL_USE_TLS")),
   "MAIL_USERNAME": config("MAIL_USERNAME"),
   "MAIL_PASSWORD": config("MAIL_PASSWORD"),
   "MAIL_DEFAULT_SENDER": config("MAIL_DEFAULT_SENDER")
}

app = Flask(__name__)
app.config.update(config)
mail = Mail(app) 

@app.route("/sendmail")
def sendmail():
    msg = Message(subject="Bem-Vindo",
                  sender=app.config["MAIL_DEFAULT_SENDER"],
                  recipients=["tiagob.tardelli@gmail.com"],
                  html=render_template("mail/welcome.html", name="Tiago")
    )
    mail.send(msg)
    return "Meu email"

 
if __name__ == "__main__":
    app.run(debug=True) 
