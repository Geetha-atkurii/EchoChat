# Echo Chat Backend 🚀

"Echo Chat" is a scalable real-time chat backend built using FastAPI and MySQL.  
The project follows clean architecture principles with proper separation of concerns (Schema, DAO, Service, Route).

This backend is being developed in phases to simulate production-level backend engineering practices.

---

## 🧠 Project Vision

Echo Chat aims to provide:

- Real-time messaging using WebSockets
- Smart message state tracking (sent, delivered, read, preview-read)
- Presence tracking (online, typing, active)
- Secure authentication with JWT
- Clean, scalable architecture

---

## 🏗 Tech Stack

- Python 3.11+
- FastAPI
- MySQL
- SQLAlchemy ORM
- Pydantic
- Uvicorn
- Passlib (Password hashing)
- Python-JOSE (JWT)
- Python-dotenv

---

## 📁 Project Structure

echo_chat/
│
├── app/
│ ├── core/ # Config, middleware, dependencies
│ ├── database/ # DB session and base setup
│ ├── common/ # Custom response handling
│ ├── modules/
│ │ └── user/ # User module (model, schema, dao, service, route)
│ └── main.py
│
├── .env
├── requirements.txt
└── README.md


---

## 🔧 Features (Completed)

- Clean project structure
- Environment-based configuration
- MySQL database integration
- SQLAlchemy ORM setup
- Custom response structure
- User model with audit fields
- Public user identifier (alphanumeric user_id)

---

## 🔜 Upcoming Features

- User Registration API
- Login API with JWT Authentication
- Email verification
- WebSocket-based real-time messaging
- Chat module
- Message module
- Presence tracking
- Read / Preview-read status tracking
- Docker configuration
- Production deployment setup

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

git clone https://github.com/your-username/echo-chat-backend.git
cd echo-chat-backend


### 2️⃣ Create Virtual Environment

python -m venv venv
venv\Scripts\activate


### 3️⃣ Install Dependencies

pip install -r requirements.txt


### 4️⃣ Configure Environment Variables

Create `.env` file in root:

DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=yourpassword
DB_NAME=echo_chat


### 5️⃣ Run Application

uvicorn app.main:app --reload


Open in browser:

http://127.0.0.1:8000


---

## 🧱 Architecture Philosophy

This project follows:

- Separation of concerns
- Layered architecture
- Service-based business logic
- DAO-based database operations
- Clean dependency injection
- Production-ready configuration management

---

## 📌 Development Approach

Each major feature is implemented in structured phases:

1. Base setup
2. User module
3. Authentication
4. Chat system
5. Real-time messaging
6. Scaling improvements

Each phase is committed separately to maintain a clean Git history.

---

## 👩‍💻 Author

Developed as part of backend system design practice and real-time system architecture learning.