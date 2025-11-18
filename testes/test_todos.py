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
    # 1. Criar
    create_resp = client.post('/todos/', json={'title': 'Update Me'}, headers=auth_header)
    todo_id = create_resp.json['id']

    # 2. Atualizar
    response = client.put(f'/todos/{todo_id}', json={
        'is_completed': True
    }, headers=auth_header)
    
    assert response.status_code == 200
    assert response.json['is_completed'] is True

def test_delete_todo(client, auth_header):
    # 1. Criar
    create_resp = client.post('/todos/', json={'title': 'Delete Me'}, headers=auth_header)
    todo_id = create_resp.json['id']

    # 2. Deletar
    response = client.delete(f'/todos/{todo_id}', headers=auth_header)
    assert response.status_code == 200

    # 3. Verificar se sumiu
    get_resp = client.get('/todos/', headers=auth_header)
    assert len(get_resp.json['data']) == 0