# 🚀 Task Manager API

![Python](https://img.shields.io/badge/python-3.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.110-green)
![Docker](https://img.shields.io/badge/docker-ready-blue)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

A modern backend service for task management with authentication, authorization, and role-based access control.

---

## 📌 About the Project

**Task Manager API** is a production-style REST API that demonstrates:

- 🔐 Secure authentication with JWT  
- 🛡 Role-based authorization (user/admin)  
- 🧩 Clean architecture (layered design)  
- ⚙️ Scalable and maintainable backend structure  

---

## 🧱 Tech Stack

- FastAPI  
- PostgreSQL  
- SQLAlchemy 2.0  
- Alembic  
- JWT (python-jose)  
- Passlib (Argon2)  
- Docker & Docker Compose  

---

## 🧭 Architecture Overview

```
Client → API Routes → Services → Repositories → Database
                 ↓
           Dependencies (Auth, DB)
```

### Layers

- **Routes** — handle HTTP requests  
- **Services** — business logic  
- **Repositories** — database access  
- **Dependencies** — reusable components (auth, db)  

---

## 📂 Project Structure

```
app/
├── api/routes/
├── core/
├── dependencies/
├── database/
├── models/
├── repositories/
├── services/
├── schemas/
├── exception/
└── main.py
```

---

## 🔐 Authentication & Authorization

### JWT Tokens
- Access Token (15 min)
- Refresh Token (7 days)

### Roles
- `user`
- `admin`

### Protection
- Auth: `Depends(get_current_user)`
- Role: `require_role(Role.admin)`

---

## 📡 API Endpoints

### Auth
- POST `/auth/register`
- POST `/auth/login`
- GET `/auth/me`

### Tasks
- GET `/tasks`
- POST `/tasks`
- PATCH `/tasks/{id}`
- DELETE `/tasks/{id}`

### Admin
- GET `/admin`

---

## ⚙️ Setup

```bash
git clone https://github.com/someboredloser/task-manager-api.git
cd task-manager-api
docker-compose up --build
```

App: http://localhost:8080  
Docs: http://localhost:8080/docs  

---

## 🔧 Environment

```
ENV=dev
DEBUG=True

DATABASE_URL=postgresql+psycopg://postgres:admin@db:5432/postgres

SECRET_KEY=supersecretkey
ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=15
REFRESH_TOKEN_EXPIRE_DAYS=7
```

---

## 🗄 Migrations

```bash
alembic revision --autogenerate -m "init"
alembic upgrade head
```

---

## 📌 Example

```bash
POST /auth/login
```

```json
{
  "email": "user@example.com",
  "password": "password"
}
```

---

## 📈 Future Improvements

- Refresh tokens endpoint  
- Pagination  
- Logging  
- Tests  
- CI/CD  

---

## 👨‍💻 Author

Backend Developer (FastAPI / Python)

---

## 📄 License

MIT
