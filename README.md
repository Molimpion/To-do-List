# 📝 Todo List API (Roadmap.sh Challenge)

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Swagger](https://img.shields.io/badge/Swagger-85EA2D?style=for-the-badge&logo=swagger&logoColor=black)
![Pytest](https://img.shields.io/badge/pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)

Este projeto é a implementação do desafio Todo List API do [roadmap.sh](https://roadmap.sh/projects/todo-list-api), construído com foco em Arquitetura Modular (Service Pattern) e Qualidade de Código.

---

### 1. Visão Geral e Estado do Projeto

- [x] Funcionalidade Central (CRUD)
- [x] Autenticação (JWT)
- [x] Paginação e Filtros
- [x] Testes Automatizados (Pytest)
- [x] Documentação Interativa (Swagger)
- [x] Arquitetura Modular (Service Pattern)

### 2. Arquitetura e Decisões de Design

- Separação por módulos (features)
- Service Pattern para lógica desacoplada
- Flask e Python para microserviços
- MySQL 8 via Docker Compose
- JWT para autenticação
- Handler de erros centralizados (__init__.py)
- DX: Rich, Flasgger

### 3. Como Executar

**Pré-requisitos:**
- Git, Docker (+Compose), Python 3.10+, venv

**Setup:**
```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

**Configuração do .env:** (veja exemplo acima)

**Banco:**
```
docker-compose up -d
```

**Rodar API:**
```
python run.py
```

### 4. Testes e Documentação

- Acesse: http://127.0.0.1:5000/docs (Swagger)
- Testes automatizados: `PYTHONPATH=. pytest`
- Testes manuais: arquivo `api.http` para REST Client

### 5. Endpoints Principais

| Método | Endpoint        | Descrição                       | Segurança           |
|--------|----------------|---------------------------------|---------------------|
| POST   | /auth/register | Cria um novo usuário            | Público             |
| POST   | /auth/login    | Autentica e retorna o JWT       | Público             |
| POST   | /todos         | Cria uma nova tarefa            | Token Obrigatório   |
| GET    | /todos         | Lista tarefas                   | Token Obrigatório   |
| PUT    | /todos/{id}    | Atualiza tarefa/status          | Token Obrigatório   |
| DELETE | /todos/{id}    | Remove uma tarefa               | Token Obrigatório   |
```
Este modelo destaca as tecnologias com badges, facilita a leitura e padroniza as informações essenciais do projeto.

[1](https://roadmap.sh/projects/todo-list-api)
[2](https://github.com/mrizkisaputra/backend-projects)
[3](https://roadmap.sh/api-design)
[4](https://www.linkedin.com/posts/roadmapsh_todo-list-api-project-idea-activity-7391635707343245312-94xX)
[5](https://bump.sh/blog/using-readme-style-api-documentation-to-enhance-your-api-design/)
[6](https://www.youtube.com/watch?v=9lS3slfJ0x0)
[7](https://roadmap.sh)
[8](https://ui.shopafzar.ir/projects/todo-list-api/solutions)
[9](https://roadmap.sh/backend/projects)
[10](https://readme.com/resources/api-documentation-essentials-from-creation-to-integration)
