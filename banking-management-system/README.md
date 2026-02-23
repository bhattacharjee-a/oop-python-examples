# 🏦 Python Banking Management System  

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Tests](https://img.shields.io/badge/tests-11%20passing-brightgreen)
![Coverage](https://img.shields.io/badge/coverage-25%25-red)
![License](https://img.shields.io/badge/license-MIT-blue)

### File-Based Backend Project using Python & OOP

A **console-based banking management system** built using **Python and Object-Oriented Programming (OOP)** principles and modern Python packaging practices (`src/` layout).

This project demonstrates **backend fundamentals**, including role-based, persistent storage, centralized logging, modular architecture, and clean project structuring.

> 🎯 Built as a **portfolio project** to showcase backend engineering skills for Python developer roles and software design skills.
> development skills.

------------------------------------------------------------------------

## 🚀 Key Features

### 🔐 Administrative Module
- Secure admin login with limited attempts
- Add / remove bank staff members
- Create & delete customer accounts
- View administrative & customer databases
- Change administrative passwords

### 👤 Customer Module
- Customer authentication
- Open new bank accounts
- View account details
- Deposit & withdraw funds
- Update personal details and password
- Secure account deletion

### 💰 Transaction Management
- Deposit validation
- Withdrawal validation (insufficient balance handling)
- Persistent balance updates using file storage

------------------------------------------------------------------------

## 🧱 Project Architecture

```
banking-management-system/
│
├── pyproject.toml
├── pytest.ini
│
├── src/
│   └── banking/
│       ├── bank.py              # Application entry & navigation
│       ├── admin.py             # Admin operations
│       ├── customer.py          # Customer operations
│       ├── account.py           # Account management logic
│       ├── transaction.py       # Deposit / withdrawal logic
│       ├── repository.py        # File-based data persistence
│       ├── constants.py         # Global configuration values
│       ├── logging_config.py    # Centralized logging setup
│       └── main.py              # Application entry point
│
├── data/
│       ├── customer_database.json         # Customer data storage
│       ├── administrative_database.json   
│       └── account_numbers.json   
│
├── run.py
├── tests/                   # Unit tests for business logic modules (basic)
├── requirements.txt     
├── LICENSE
└── README.md
```

## 📐 Architecture Overview

The system follows a layered modular architecture:
                ┌──────────────────────┐
                │      CLI Layer       │
                │  (main.py / run.py)  │
                └──────────┬───────────┘
                           │
                ┌──────────▼───────────┐
                │   Service Layer      │
                │  bank.py / admin.py  │
                │  customer.py         │
                └──────────┬───────────┘
                           │
                ┌──────────▼───────────┐
                │  Domain Layer        │
                │ account.py           │
                │ transaction.py       │
                └──────────┬───────────┘
                           │
                ┌──────────▼───────────┐
                │ Persistence Layer    │
                │ repository.py        │
                │ JSON storage         │
                └──────────────────────┘

------------------------------------------------------------------------

## 🛠️ Technologies Used
- **Python 3**
- **JSON** (file-based persistence)
- **Logging module**
- **Object-Oriented Programming (OOP)**

---

## 🧠 Design Highlights
- Modular architecture with separation of concerns
- Centralized logging (file + console)
- Configurable constants
- Role-based access control (Admin / Customer)
- Defensive programming (input validation, attempt limits)

---

## ⚠️ Known Limitations
- Console-based interface (CLI)
- Passwords stored in plain text (for demonstration only)
- JSON used instead of a database
- Business logic tightly coupled with CLI input

These trade-offs were intentional to keep the project focused on **core backend fundamentals**.

---

## 📌 Future Improvements
- Replace JSON storage with SQLite / PostgreSQL
- Add password hashing
- Decouple UI from business logic
- Expose functionality via REST API (Flask / FastAPI)
- Improve unit test coverage

------------------------------------------------------------------------

## 📦 Installation

Create virtual environment:

    python -m venv venv

Activate environment (Windows):

    venv\Scripts\activate

Install project in editable mode:

    pip install -e .

Install test dependencies:

    pip install -r requirements.txt

------------------------------------------------------------------------
## ▶️ How to Run

After installation:

    banking-management-system

Alternative:

    ```bash
    python run.py
        or
    python main.py
    ```

------------------------------------------------------------------------

## 🧪 Run Tests

    pytest

------------------------------------------------------------------------
## ▶️ How to Run

```bash
python main.py
```

---

## 👨‍💻 Author
**Bhattacharjee**  
Python Developer | Backend & OOP Enthusiast
