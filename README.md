# CineReserve API

Uma API RESTful moderna para gerenciamento de reservas em cinemas, desenvolvida com Django Rest Framework.

## 🎬 Sobre o Projeto

CineReserve é uma solução completa para sistema de reservas em cinemas. A API fornece funcionalidades para:

- ✅ Autenticação e gerenciamento de usuários
- ✅ Gestão de filmes em cartaz
- ✅ Salas de cinema e assentos
- ✅ Sessões de filmes programadas
- ✅ Sistema de reservas de assentos
- ✅ Documentação interativa com Swagger/OpenAPI

## 🚀 Tecnologias

- **Django** 6.0.3+ - Framework web robusto para Python
- **Django REST Framework** 3.16.1+ - Toolkit para construção de APIs REST
- **PostgreSQL** - Banco de dados relacional
- **JWT (Simple JWT)** 5.5.1+ - Autenticação baseada em tokens
- **drf-spectacular** 0.29.0+ - Documentação OpenAPI/Swagger automática
- **Poetry** - Gerenciamento de dependências

## 📋 Pré-requisitos

- Python 3.14+
- PostgreSQL 12+
- Poetry (gerenciador de pacotes Python)
- Virtual Environment

## 🔧 Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/miguelwilliam/CineReserve-API.git
cd CineReserve-API
```

### 2. Configure o ambiente virtual

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3. Instale as dependências

```bash
poetry install
```

Ou, se estiver usando apenas pip:

```bash
pip install -r requirements.txt
```

### 4. Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
# Django
DEBUG=True
SECRET_KEY=sua-chave-secreta-aqui

# Database
DB_ENGINE=django.db.backends.postgresql
DB_NAME=cinereserve_db
DB_USER=seu_usuario_db
DB_PASSWORD=sua_senha_db
DB_HOST=localhost
DB_PORT=5432
```

### 5. Configure o banco de dados

```bash
# Execute as migrações
python manage.py migrate

# Crie um superusuário (opcional)
python manage.py createsuperuser
```

### 6. Inicie o servidor

```bash
python manage.py runserver
```

O servidor estará disponível em: `http://localhost:8000`

## 📚 Documentação da API

A documentação interativa está disponível em:

- **Swagger UI**: `http://localhost:8000/api/docs/`
- **OpenAPI Schema (JSON)**: `http://localhost:8000/api/schema/`

## 🔐 Autenticação

A API utiliza autenticação JWT (JSON Web Tokens). 

### Obtendo um Token

```bash
POST /api/user/token/
Content-Type: application/json

{
  "email": "usuario@example.com",
  "password": "sua_senha"
}
```

**Resposta:**
```json
{
  "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
```

### Usando o Token

Inclua o token no header `Authorization`:

```bash
GET /api/movies/
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...
```

### Refrescando o Token

```bash
POST /api/user/token/refresh/
Content-Type: application/json

{
  "refresh": "seu_refresh_token"
}
```


## 🏗️ Estrutura do Projeto

```
CineReserve-API/
├── api/
│   ├── models/               # Modelos de dados
│   │   ├── user.py          # Modelo de usuário
│   │   ├── movie.py         # Modelo de filme
│   │   ├── room.py          # Modelo de sala
│   │   ├── seat.py          # Modelo de assento
│   │   ├── session.py       # Modelo de sessão
│   │   ├── reservation.py   # Modelo de reserva
│   │   └── sessionseat.py   # Modelo de assento da sessão
│   ├── views/                # Views e viewsets da API
│   ├── serializers/          # Serializadores DRF
│   ├── migrations/           # Migrações do banco de dados
│   ├── urls.py              # Rotas da API
│   ├── admin.py             # Configuração do admin
│   └── signals.py           # Signals do Django
├── config/
│   ├── settings.py          # Configurações do Django
│   ├── urls.py              # Rotas principais
│   ├── wsgi.py              # Configuração WSGI
│   └── asgi.py              # Configuração ASGI
├── manage.py                # Script de gerenciamento Django
├── pyproject.toml           # Configuração do Poetry
└── db.sqlite3               # Banco de dados (desenvolvimento)
```

## 🔒 Segurança

- ✅ Senhas criptografadas com PBKDF2
- ✅ Rate limiting em autenticação
- ✅ CORS configurável
- ✅ Proteção CSRF
- ✅ JWT Token com expiração
- ✅ Variáveis sensíveis em `.env`


## 📦 Dependências Principais

| Pacote | Versão |
|--------|--------|
| django | >=6.0.3 |
| djangorestframework | >=3.16.1 |
| djangorestframework-simplejwt | >=5.5.1 |
| drf-spectacular | >=0.29.0 |
| psycopg[binary] | >=3.3.3 |
| environs | >=14.6.0 |


## 📄 Licença

Este projeto está licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 👤 Autor

**Miguel William**
- GitHub: [@miguelwilliam](https://github.com/miguelwilliam)

**Esse README foi feito com ajuda do Github Copilot e está sujeito a erros!**

**Desenvolvido com ❤️ usando Django e Django REST Framework**