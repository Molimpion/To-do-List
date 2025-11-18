# 📝 Todo List API (Roadmap.sh Challenge)

<div align="center">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=py,flask,mysql,docker,swagger,pytest" />
  </a>
</div>

Este projeto é a implementação do desafio Todo List API do [roadmap.sh](https://roadmap.sh/projects/todo-list-api), desenvolvido com arquitetura modular e código limpo.

---

### Visão Geral do Projeto

- API RESTful para tarefas pessoais
- Padrão Modular e Service Pattern implementados
- CRUD, autenticação JWT, filtros e testes
- Documentação Swagger + testes Pytest

---

### Arquitetura & Design

- **Módulos organizados:** auth e todos, isolamento em services
- **Banco:** MySQL 8.0, dockerizado
- **Autenticação:** JWT, segurança por werkzeug
- **DX:** Rich (logs), Flasgger (docs)

---

### Como Executar

**1. Pré-requisitos:**  
Git, Docker, Python >=3.10, venv

**2. Setup:**  
- Clone, crie venv e instale dependências
- Configure o arquivo `.env`  
- Suba o banco com `docker-compose up -d`  
- Rode `python run.py`

---

### Testes & Documentação

- Swagger: [http://127.0.0.1:5000/docs](http://127.0.0.1:5000/docs)  
- Testes: `PYTHONPATH=. pytest`  
- Testes manuais: arquivo `api.http` completo

---

### Endpoints Principais

| Método | Endpoint        | Descrição                       | Segurança           |
|--------|----------------|---------------------------------|---------------------|
| POST   | /auth/register | Cria um novo usuário            | Público             |
| POST   | /auth/login    | Autentica e retorna o JWT       | Público             |
| POST   | /todos         | Cria uma nova tarefa            | Token Obrigatório   |
| GET    | /todos         | Lista tarefas                   | Token Obrigatório   |
| PUT    | /todos/{id}    | Atualiza tarefa/status          | Token Obrigatório   |
| DELETE | /todos/{id}    | Remove uma tarefa               | Token Obrigatório   |
