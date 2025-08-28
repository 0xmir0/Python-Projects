# Student DB Manager (CLI)

A simple **command-line student management system** written in Python.  
This project was built **for practice** in logic and database handling.  
It uses **SQLite** for storing student data, including grades, absence records, and payment tracking.  
No GUI is provided — everything is accessible from the terminal through a menu-driven interface.

---

## Features

- **Student Records**
  - Add new students (name, grade, paid months, absent days)
  - Search students by ID
  - List all students in a specific grade

- **Absence Tracking**
  - Mark absence for individual students
  - Mark absence for multiple students
  - View all students’ absence records

- **Payments**
  - Store months paid per student
  - List students who paid for a given month and grade
  - (Placeholders exist for money collection and payment checks)

- **General**
  - Menu-driven navigation
  - Graceful exit with `Ctrl + C`

---
