# 🚆 Train Reservation System

![Python](https://img.shields.io/badge/Python-3.12-blue)
![OOP](https://img.shields.io/badge/Paradigm-OOP-green)
![Status](https://img.shields.io/badge/Project-Completed-brightgreen)
![Level](https://img.shields.io/badge/Level-Beginner-lightgrey)

git add README.md
git commit -m "Added project badges to README"
git pushA simple **console-based Train Reservation System built using Python classes and basic OOP concepts**.

It demonstrates:
- Class creation
- Instance attributes
- File handling
- Basic seat booking logic
- Conditional flow control

This project reflects foundational stage before progressing to more structured backend systems (see Banking System project for evolution).

------------------------------------------------------------------------

## 📌 Features

- Two trains available (Rajdhani & Duronto)
-   View train details
-   Check available seats
-   Book seats
-   Cancel booked seats
-   File-based persistent seat storage
-   Console-based user interaction

------------------------------------------------------------------------

## 🏗 Architecture Overview

This project follows a simple, single-class architecture:

-   `Train` class encapsulates:
    -   Train metadata (name, number, total seats, fare)
    -   Seat availability logic
    -   Booking logic
    -   Cancellation logic
-   File-based storage simulates persistent seat management
-   Console inputs handle user interaction
-   Source code and runtime data are separated structurally

The simplicity of this architecture reflects an early OOP before introducing:

-   Modularization
-   Logging systems
-   Exception handling layers
-   Service/repository separation

Those concepts are demonstrated in later projects.

------------------------------------------------------------------------

## 📂 Project Structure

    train-reservation-system/
    │
    ├── src/
    │   └── train.py              # Main application logic
    │
    ├── data/                     # Stores seat booking files (auto-created)
    │
    ├── README.md
    └── .gitignore

### Folder Explanation

-   **src/** → Contains the application source code\
-   **data/** → Stores `.txt` files that persist seat bookings\
-   **README.md** → Project documentation\
-   **.gitignore** → Prevents unnecessary files from being tracked

------------------------------------------------------------------------

## ⚙️ Technologies Used

-   Python 3
-   Object-Oriented Programming (OOP)
-   File Handling (`a+` mode for persistence)
-   Basic Control Flow

No external dependencies are required.

------------------------------------------------------------------------

## ▶️ How to Run

```bash
1.  Navigate to the project root directory.
2.  Run:

```{=html}
<!-- -->
```bash

    python src/train.py         🚆 Train Booking System (First OOP Project)

Make sure the `data/` folder exists.\
Text files will be automatically created when booking seats.


------------------------------------------------------------------------

## 🚀 Future Improvements (Intentionally Not Implemented Here)

-   Input validation using exception handling
-   Logging system integration
-   Modular file separation
-   Database-backed storage
-   REST API interface

These improvements are demonstrated in later, more advanced projects.

------------------------------------------------------------------------

## 📌 Author
**Bhattacharjee**  

Built as part of Python and GitHub learning journey, focusied on
writing clean, incremental, and evolution-driven projects.
