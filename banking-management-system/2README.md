# 🏦 Banking Management System

### File-Based Backend System using Python & Object-Oriented Programming

A modular console-based banking backend built using modern Python
packaging practices (`src/` layout).\
This project demonstrates backend engineering fundamentals including
role-based access control, persistent storage, logging, and clean
modular architecture.

> Built as a portfolio-ready backend project to demonstrate Python
> development skills.

------------------------------------------------------------------------

## 🚀 Key Features

### 🔐 Administrative Module

-   Secure admin login with limited attempts
-   Add / remove bank staff members
-   Create & delete customer accounts
-   View administrative & customer databases
-   Change administrative passwords

### 👤 Customer Module

-   Customer authentication
-   Open new bank accounts
-   View account details
-   Deposit & withdraw funds
-   Update personal details and password
-   Secure account deletion

### 💰 Transaction Management

-   Deposit validation
-   Withdrawal validation with insufficient balance handling
-   Persistent balance updates using JSON storage

------------------------------------------------------------------------

## 🧱 Project Architecture

    banking-management-system/
    │
    ├── run.py
    ├── pyproject.toml
    ├── requirements.txt
    ├── pytest.ini
    │
    ├── src/
    │   └── banking/
    │       ├── bank.py
    │       ├── admin.py
    │       ├── customer.py
    │       ├── account.py
    │       ├── transaction.py
    │       ├── repository.py
    │       ├── constants.py
    │       ├── logging_config.py
    │       └── main.py
    │
    ├── tests/
    └── data/

------------------------------------------------------------------------

## 🛠 Technologies Used

-   Python 3
-   JSON (file-based persistence)
-   Logging module
-   Object-Oriented Programming (OOP)
-   Pytest (for unit testing)

------------------------------------------------------------------------

## 🧠 Design Highlights

-   `src/` layout for clean packaging
-   Modular separation of concerns
-   Centralized logging (file + console)
-   Configurable constants
-   Defensive programming (validation & attempt limits)
-   Installable CLI entry point

------------------------------------------------------------------------

## ⚠️ Known Limitations

-   CLI-based interface
-   Plain-text password storage (demonstration only)
-   JSON instead of production database
-   Business logic partially coupled with CLI input

------------------------------------------------------------------------

## 🔮 Future Improvements

-   Password hashing (bcrypt)
-   SQLite or PostgreSQL backend
-   REST API using FastAPI
-   CI/CD integration
-   Improved unit test coverage

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

## ▶️ Run Application

After installation:

    banking-management-system

Alternative:

    python run.py

------------------------------------------------------------------------

## 🧪 Run Tests

    pytest

------------------------------------------------------------------------

## 👨‍💻 Author

Bhattacharjee\
Backend-Focused Python Developer
