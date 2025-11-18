import pytest
from src import create_app
from src.extensions import db

@pytest.fixture
def app():
    # Cria o app usando SQLite em memória para ser RÁPIDO e isolado
    app = create_app({
        'TESTING': True,
        'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:',
        'JWT_SECRET_KEY': 'test_secret_key'
    })

    with app.app_context():
        db.create_all()  
        yield app
        db.session.remove()
        db.drop_all()    

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def auth_header(client):
    """Fixture auxiliar para registrar, logar e retornar o token pronto"""
    # 1. Registrar
    client.post('/auth/register', json={
        'username': 'tester',
        'password': 'password123'
    })
    # 2. Login
    response = client.post('/auth/login', json={
        'username': 'tester',
        'password': 'password123'
    })
    token = response.json['access_token']
    return {'Authorization': f'Bearer {token}'}