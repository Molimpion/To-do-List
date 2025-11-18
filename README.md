# 🐍 Todo List API (Desafio Roadmap.sh)

-----

*Este projeto é a implementação do desafio **Todo List API** do [roadmap.sh](https://roadmap.sh/projects/todo-list-api), construído com foco em **Arquitetura Modular (Service Pattern)** e **Qualidade de Código**.*

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)

## 1\. Visão Geral e Estado do Projeto

Este repositório contém uma **API RESTful** completa para gerenciamento de tarefas pessoais. O objetivo principal foi cumprir o desafio do roadmap.sh e, adicionalmente, aplicar padrões de projetos vistos no mercado (como Service Pattern e Logs estruturados).

Todos os requisitos funcionais do backend foram **concluídos, documentados com Swagger e validados por testes automatizados**.

  * [x] **Funcionalidade Central (CRUD):** Completo
  * [x] **Autenticação (JWT):** Completo
  * [x] **Paginação e Filtros:** Completo
  * [x] **Testes Automatizados (Pytest):** Completo
  * [x] **Documentação Interativa (Swagger):** Completo
  * [x] **Arquitetura Modular (Service Pattern):** Completo

-----

## 2\. Arquitetura e Decisões de Design

A aplicação segue o padrão **Modular (Feature-Based)** para maximizar a testabilidade e o reuso de código:

  * **Padrão Service:** Toda a lógica de negócio (*hashing*, validação de dados, consultas ao banco) está isolada na camada **Service**. As rotas (`routes.py`) apenas lidam com a camada HTTP.
  * **Tratamento de Erros:** Sistema centralizado no `__init__.py` que captura todas as exceções personalizadas (`AuthError`, `NotFoundError`) e as transforma em respostas JSON padronizadas.
  * **Banco de Dados:** MySQL 8.0, orquestrado via **Docker Compose**.
  * **Developer Experience (DX):** Uso da biblioteca **Rich** para logs coloridos e tracebacks formatados no terminal.
  * **QA:** Uso de **Pytest** com banco de dados SQLite em memória (`:memory:`) para garantir que os testes sejam rápidos e isolados.

-----

## 3\. Como Executar o Projeto Localmente

O ambiente é padronizado via Docker para o banco de dados e o Python roda em `venv`.

### 1\. Pré-requisitos

  * Git
  * Docker e Docker Compose (para o MySQL)
  * Python 3.10+ e `venv`

### 2\. Setup e Inicialização

1.  **Clone o repositório, crie e ative o ambiente virtual.**
2.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Crie o arquivo `.env`** na raiz do projeto (importante para as credenciais).
4.  **Inicie o Banco de Dados (MySQL):**
    ```bash
    docker-compose up -d
    ```
5.  **Inicie a Aplicação Flask:**
    ```bash
    python run.py
    ```
    *O terminal mostrará um link clicável para a documentação via Rich.*

-----

## 4\. Testes e Documentação

### 4.1. Testes Automatizados (Pytest) 🧪

Para executar o conjunto de testes (8 testes unitários e de integração), use o comando com `PYTHONPATH` para resolver as importações modulares:

```bash
PYTHONPATH=. pytest
```

*A saída deve ser `8 passed`, confirmando a estabilidade do sistema.*

### 4.2. Documentação Interativa (Swagger UI) 📄

A documentação visual e interativa está disponível em: `http://127.0.0.1:5000/docs`

1.  **Login:** Use o endpoint `/auth/login` para obter o `access_token`.
2.  **Autorização:** Clique em **"Authorize"** e insira o token no formato: `Bearer [SEU_TOKEN_AQUI]`.
3.  Execute o CRUD completo na interface do Swagger.

-----

## 5\. Endpoints Principais

| Método | Endpoint | Descrição | Segurança |
| :--- | :--- | :--- | :--- |
| `POST` | `/auth/register` | Cria um novo usuário | Público |
| `POST` | `/auth/login` | Autentica e retorna o JWT | Público |
| `POST` | `/todos` | Cria uma nova tarefa | **Token Obrigatório** |
| `GET` | `/todos` | Lista tarefas (com Paginação e Filtros `?status=`) | **Token Obrigatório** |
| `PUT` | `/todos/{id}` | Atualiza o conteúdo ou status (`is_completed`) | **Token Obrigatório** |
| `DELETE` | `/todos/{id}` | Remove uma tarefa | **Token Obrigatório** |


Aqui estão duas versões profissionais para destacar o README.md do seu projeto Todo List API, ambas inspiradas em projetos de alto padrão e adaptadas ao seu contexto.

***

## Versão 1: Badges Corporativos (Shields.io) – Foco em Stack e Status

```markdown
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

<!-- Lista de requisitos -->
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

***

## Versão 2: Visual Moderno com Skill Icons – Foco em Stack Imediato e Experiência

```markdown
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
```

***

Essas duas estruturas estão entre as mais apreciadas em projetos open source de qualidade e vão valorizar ainda mais o seu repositório. Você pode alternar entre o visual mais “corporativo” do Shields.io ou o impacto moderno e direto dos Skill Icons, sempre com tabelas e divisão lógica das seções.[1][2][3][4][5]

[1](https://github.com/tandpfun/skill-icons)
[2](https://github.com/gui-bus/TechIcons)
[3](https://skillicons.dev)
[4](https://github.com/cfprocha/distintivos)
[5](https://apidog.com/pt/blog/api-documentation-best-practices-and-tools-pt/)
