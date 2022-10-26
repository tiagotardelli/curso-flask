from . import email
from app import mail
from decouple import config
from flask_mail import Mail, Message

@email.route("/sendmail")
def sendemail():
    
    msg = Message(subject="Bem-vindo", 
                  sender=config("MAIL_DEFAULT_SENDER"),
                  recipients="tiagob.tardelli@gmail.com",
                  body="Apenas mais um e-mail enviado de um SMTP faker"
    )
    
    mail.send(msg)
    
    return "E-mail enviado com sucesso!"