import pytest
from app import create_app, db
from app.models import User

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///"
    app.config["WTF_CSRF_ENABLED"] = False

    context = app.app_context()
    context.push()

    db.create_all()

    yield app.test_client()

    db.session.remove()
    db.drop_all()

    context.pop()


def test_se_pagina_usuario_retorna_code_200(client):
    response = client.get("/")
    assert response.status_code == 200

def test_se_link_registrar_existe(client):
    response = client.get("/")
    assert "Registrar" in response.get_data(as_text=True) 

def test_se_link_login_existe(client):
    response = client.get("/")
    assert "Login" in response.get_data(as_text=True) 

def test_registrando_usuario(client):
    data = {
        "name": "Amanda",
        "email": "amanda@gmail.com",
        "password": "12345"
    }
    response = client.post("/register", data=data, follow_redirects=True)
    assert "Amanda" in response.get_data(as_text=True)

def test_logondo_usuario(client):
    data = {
        "name": "Amanda",
        "email": "amanda@gmail.com",
        "password": "12345"
    }
    client.post("/register", data=data, follow_redirects=True)
    
    response = client.post("/login", data=data, follow_redirects=True)
    assert "Sair" in response.get_data(as_text=True)
