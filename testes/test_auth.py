def test_register_success(client):
    response = client.post('/auth/register', json={
        'username': 'newuser',
        'password': 'securepassword'
    })
    assert response.status_code == 201
    assert response.json['msg'] == "Usuário criado com sucesso"

def test_register_missing_data(client):
    """Teste de Falha: Tentar registrar sem senha"""
    response = client.post('/auth/register', json={
        'username': 'incomplete_user'
    })
    assert response.status_code == 400
    assert response.json['error'] is True

def test_register_duplicate_user(client):
    """Teste de Falha: Tentar registrar usuário já existente"""
    client.post('/auth/register', json={'username': 'u1', 'password': 'p1'})
    
    response = client.post('/auth/register', json={'username': 'u1', 'password': 'p1'})
    assert response.status_code == 409

def test_login_success(client):
    client.post('/auth/register', json={'username': 'u2', 'password': 'p2'})
    
    response = client.post('/auth/login', json={
        'username': 'u2',
        'password': 'p2'
    })
    assert response.status_code == 200
    assert 'access_token' in response.json

def test_login_missing_data(client):
    """Teste de Falha: Tentar logar sem username"""
    response = client.post('/auth/login', json={
        'password': 'somepassword'
    })
    assert response.status_code == 400

def test_login_fail_credentials(client):
    """Teste de Falha: Senha ou usuário incorretos"""
    response = client.post('/auth/login', json={
        'username': 'nonexistent',
        'password': 'wrong'
    })
    assert response.status_code == 401