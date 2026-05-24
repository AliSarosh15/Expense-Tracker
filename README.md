# 💰 Expense Tracker API

A RESTful Expense Tracking API built using **Flask, SQLAlchemy, and PostgreSQL** that allows users to manage expenses, categories, and personal financial records with token-based authentication.

This project demonstrates backend API development, authentication, relational database management, and CRUD operations using Flask.

---

# 🚀 Features

✅ User Authentication  
✅ Token-Based Authorization  
✅ Expense Management APIs  
✅ Category Management APIs  
✅ User Management APIs  
✅ PostgreSQL Database Integration  
✅ SQLAlchemy ORM Support  
✅ Protected Routes using Decorators  
✅ Expense Filtering by Category  
✅ Relational Database Design  
✅ REST API Architecture  

---

# 🔐 Authentication System

The project uses:

- Token-Based Authentication
- Protected API Routes
- Custom Authentication Decorators
- Session-less Authorization

### Login Flow

```text
User Login → Generate Token → Access Protected APIs
```

---

# 🛠️ Tech Stack

## ⚙️ Backend

- Python
- Flask
- Flask-SQLAlchemy
- SQLAlchemy

## 🗄️ Database

- PostgreSQL

## 🔑 Authentication

- Token-Based Authentication
- Python Secrets Module

## 🌱 Environment Management

- python-dotenv

---

# 📂 Project Structure

```text
Expense-Tracke/
│
├── newapp.py
├── requirements.txt
├── test.py
├── .gitignore
├── .env
└── expenv/
```

---

# 🗄️ Database Models

---

## 👤 User Model

```python
User(
    id,
    user_name,
    email,
    password_hash,
    token
)
```

---

## 📁 Category Model

```python
Category(
    id,
    name
)
```

---

## 💰 Expense Model

```python
Expense(
    id,
    title,
    amount,
    date,
    user_id,
    category_id
)
```

---

# ⚙️ Installation

---

## 1️⃣ Clone Repository

```bash
git clone https://github.com/AliSarosh15/Expense-Tracke.git

cd Expense-Tracke
```

---

## 2️⃣ Create Virtual Environment

```bash
python -m venv expenv
```

### Activate Environment

#### Linux / MacOS

```bash
source expenv/bin/activate
```

#### Windows

```bash
expenv\Scripts\activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the root directory.

Example:

```env
DATABASE_URL=postgresql://username:password@localhost/expense_db
```

---

# ▶️ Run The Project

```bash
python newapp.py
```

Flask server will start on:

```text
http://127.0.0.1:5000
```

---

# 📡 API Endpoints

---

# 🔐 Authentication APIs

## Login

```http
POST /api/login
```

## Logout

```http
GET /api/logout
```

---

# 👤 User APIs

## Get All Users

```http
GET /api/alluser
```

## Get User By ID

```http
GET /api/getuser/<id>
```

## Create User

```http
POST /api/postuser
```

## Update User

```http
PUT /api/putuser/<id>
```

## Delete User

```http
DELETE /api/deleteuser/<id>
```

---

# 📁 Category APIs

## Get All Categories

```http
GET /api/allcategory
```

## Get Category By ID

```http
GET /api/cat/<id>
```

## Create Category

```http
POST /api/postcat
```

## Update Category

```http
PUT /api/putcat/<id>
```

## Delete Category

```http
DELETE /api/deletecat/<id>
```

---

# 💰 Expense APIs

## Get All Expenses

```http
GET /api/getexp
```

## Create Expense

```http
POST /api/postexp
```

## Update Expense

```http
PUT /api/updateexp/<id>
```

## Delete Expense

```http
DELETE /api/deleteexp/<id>
```

---

# 🔍 Advanced Expense Queries

## Get Expenses with Category Names

```http
GET /api/getexpcat
```

---

## Get Expenses by Category Name

```http
GET /api/getexpname/<name>
```

Example:

```text
/api/getexpname/Food
```

---

# 🧠 Concepts Used

This project demonstrates:

- REST API Development
- Flask Application Structure
- SQLAlchemy ORM
- Database Relationships
- Authentication Decorators
- CRUD Operations
- Foreign Key Relationships
- Token-Based Security
- Environment Variable Management

---

# 📊 Database Relationships

```text
User ───< Expense >─── Category
```

- One User can have multiple Expenses
- One Category can contain multiple Expenses

---

# 📌 Sample Login Request

```json
{
  "user_name": "Ali",
  "password_hash": "123456"
}
```

---

# 📌 Sample Response

```json
{
  "token": "a1b2c3d4e5f6..."
}
```

---

# 🔐 Protected Routes

Protected APIs require:

```http
Authorization: Bearer <token>
```

Example:

```http
Authorization: Bearer abcd1234token
```

---

# 📈 Future Improvements

✅ Password Hashing using bcrypt  
✅ JWT Authentication  
✅ Expense Analytics Dashboard  
✅ Monthly Expense Reports  
✅ Pagination Support  
✅ Swagger API Documentation  
✅ Flask Blueprints  
✅ Docker Deployment  
✅ User-Specific Expense Filtering  
✅ Role-Based Access Control  

---

# 💡 Use Cases

- Personal Expense Tracking
- Budget Management Systems
- Financial Record APIs
- Beginner Flask Backend Projects
- Learning Authentication Systems
- CRUD API Practice

---

# 📚 Key Learnings

This project helped in understanding:

- Flask Backend Development
- SQLAlchemy Relationships
- Token-Based Authentication
- Protected API Routes
- PostgreSQL Integration
- CRUD API Design
- Environment Variables using dotenv

---

# 🤝 Contributing

Contributions are welcome.

## Steps

```bash
Fork → Clone → Create Branch → Commit → Push → Pull Request
```

---

# 📜 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

## Ali Sarosh

🎓 BTech CSE Student  
💻 Backend Developer (Python)  
🚀 Open Source Contributor  

### Interests

- Backend Development
- Flask & FastAPI
- Databases
- SQLAlchemy
- REST APIs
- AI/ML Applications

---

# 🔗 Connect With Me

## GitHub

https://github.com/AliSarosh15

## LinkedIn

https://www.linkedin.com/in/ali-sarosh-332b90280/

---

# ⭐ Support

If you found this project useful:

- ⭐ Star the repository
- 🍴 Fork the project
- 🧠 Share feedback & suggestions

---

# 📌 Final Note

Expense Tracker API is a backend-focused Flask project designed to demonstrate authentication, database relationships, and RESTful API development using PostgreSQL and SQLAlchemy in a real-world expense management system.
