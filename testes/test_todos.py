def test_create_todo(client, auth_header):
    response = client.post('/todos/', json={
        'title': 'Testar API com Pytest',
        'description': 'Escrever testes unitários'
    }, headers=auth_header)
    
    assert response.status_code == 201
    assert response.json['title'] == 'Testar API com Pytest'

def test_list_todos_empty(client, auth_header):
    response = client.get('/todos/', headers=auth_header)
    assert response.status_code == 200
    assert len(response.json['data']) == 0

def test_update_todo(client, auth_header):
    create_resp = client.post('/todos/', json={'title': 'Update Me'}, headers=auth_header)
    todo_id = create_resp.json['id']

    response = client.put(f'/todos/{todo_id}', json={
        'is_completed': True
    }, headers=auth_header)
    
    assert response.status_code == 200
    assert response.json['is_completed'] is True

def test_delete_todo(client, auth_header):
    create_resp = client.post('/todos/', json={'title': 'Delete Me'}, headers=auth_header)
    todo_id = create_resp.json['id']

    response = client.delete(f'/todos/{todo_id}', headers=auth_header)
    assert response.status_code == 200

    get_resp = client.get('/todos/', headers=auth_header)
    assert len(get_resp.json['data']) == 0

def test_create_todo_missing_title(client, auth_header):
    response = client.post('/todos/', json={
        'description': 'Tarefa sem titulo não pode'
    }, headers=auth_header)
    
    assert response.status_code == 400

def test_update_todo_not_found(client, auth_header):
    response = client.put('/todos/99999', json={
        'title': 'Isso nao existe'
    }, headers=auth_header)
    
    assert response.status_code == 404

def test_delete_todo_not_found(client, auth_header):
    response = client.delete('/todos/99999', headers=auth_header)
    
    assert response.status_code == 404

def test_update_todo_from_another_user(client, auth_header):
    create_resp = client.post('/todos/', json={'title': 'User 1 Task'}, headers=auth_header)
    todo_id = create_resp.json['id']

    client.post('/auth/register', json={'username': 'hacker', 'password': '123'})
    login_resp = client.post('/auth/login', json={'username': 'hacker', 'password': '123'})
    token_user_2 = login_resp.json['access_token']
    header_user_2 = {'Authorization': f'Bearer {token_user_2}'}

    response = client.put(f'/todos/{todo_id}', json={'title': 'Hacked'}, headers=header_user_2)
    
    assert response.status_code == 404