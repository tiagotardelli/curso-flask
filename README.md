# curso-flask
Estudando Flask

# Introdução
- Básico do Flask

# Database (SQL Alchemy) 

```console
/database    
    set FLASK_APP=app
    flask shell
    from app import db
    db.create_all()
```

```console
#Inserindo usuários no banco de dados
 /database   
    flask shell
    from app import db, User
    user = User()
    user.name = "tt"
    user.email = "tt@tt.com.br"
    user.password = "12345"
    db.session.add(user)
    db.session.commit()

    user1 = User(name="Tede", email="tade@tade.com", password="1234")
    db.session.add(user1)
    db.session.commit()

    user1 = User(name="Amanda", email="1@tade.com", password="1234")
    user2 = User(name="Ramiro", email="2@tade.com", password="1234")
    user3 = User(name="Raimunada", email="3@tade.com", password="1234")
    user4 = User(name="Betão", email="4@tade.com", password="1234")
    user5 = User(name="Caio", email="5@tade.com", password="1234")
    user6 = User(name="Carlos", email="6@tade.com", password="1234")
    user7 = User(name="Tadeu", email="7@tade.com", password="1234")

```

```console
#Inserindo usuários no banco de dados
 /database   
    flask shell
    from app import db, User, Profile

    user1 = User(name="Amanda", email="1@tade.com", password="1234")
    profile1 = Profile(name='Adm', photo='amanda.jpg', user_id=user1.id)
    user2 = User(name="Ramiro", email="2@tade.com", password="1234")
    profile2 = Profile(name='Usu', photo='ramiro.jpg', user_id=user1.id)
    db.session.add(user1)
    db.session.add(user2)
    db.session.commit()
    db.session.add(profile1)
    db.session.add(profile2)
    db.session.commit()
    
```
