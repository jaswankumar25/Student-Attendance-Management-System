# Attendify – Student Attendance Management System

A web-based Student Attendance Management System developed as a Database Management System (DBMS) project using Flask and MySQL.

---

## 📌 Project Overview

**Attendify** is a database-driven web application designed to simplify the management of student attendance.

The application provides a centralized system for managing student details, subjects, attendance records, and attendance reports through a simple and user-friendly dashboard.

The project demonstrates the practical implementation of database concepts such as data storage, retrieval, insertion, updating, and relationship-based management using **MySQL**.

---

## 🎯 Objectives

The main objectives of Attendify are:

- To maintain student information digitally.
- To manage subjects efficiently.
- To record and manage student attendance.
- To provide attendance reports.
- To reduce manual attendance management.
- To provide quick access to attendance information.
- To demonstrate the practical use of DBMS concepts in a real-world application.

---

## ✨ Key Features

### 👨‍🎓 Student Management
- Add new students.
- View student details.
- Edit existing student information.
- Manage student records in the database.

### 📚 Subject Management
- Add subjects.
- View available subjects.
- Maintain subject information.

### ✅ Attendance Management
- Record student attendance.
- Manage attendance records.
- View attendance information.
- Maintain attendance data using MySQL.

### 📊 Attendance Reports
- View attendance-related information.
- Generate attendance reports from stored database records.

### 🖥️ Dashboard
- Provides an overview of the attendance management system.
- Displays important information in a simple and organized interface.
- Provides navigation to different modules of the application.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Backend programming |
| Flask | Web application framework |
| MySQL | Database management |
| HTML | Web page structure |
| CSS | User interface styling |
| JavaScript | Client-side functionality |
| Git | Version control |
| GitHub | Source code hosting |
| Visual Studio Code | Development environment |

---

## 🏗️ System Architecture

The application follows a simple three-layer architecture:

```text
┌──────────────────────────────┐
│          Frontend            │
│       HTML + CSS + JS        │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│           Backend            │
│       Python + Flask         │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│          Database            │
│           MySQL              │
└──────────────────────────────┘
```

The user interacts with the web interface, Flask processes the application requests, and MySQL stores and retrieves the required data.

---

## 📂 Project Structure

```text
Student-Attendance-Management-System/
│
├── app.py
│
├── static/
│   └── style.css
│
├── templates/
│   ├── index.html
│   ├── add_student.html
│   ├── edit_student.html
│   ├── students.html
│   ├── add_subject.html
│   ├── subjects.html
│   ├── attendance.html
│   └── reports.html
│
├── .gitignore
└── README.md
```

> The `venv` virtual environment is used locally for Python dependencies and is excluded from GitHub using `.gitignore`.

---

## 🗄️ Database

Attendify uses **MySQL** as its database management system.

The database is responsible for storing and managing information related to:

- Students
- Subjects
- Attendance records

The Flask backend communicates with the MySQL database to perform database operations such as:

- `INSERT`
- `SELECT`
- `UPDATE`
- `DELETE`

This allows the application to provide real-time interaction with the stored data.

---

## 🔄 Application Workflow

```text
User
  │
  ▼
Attendify Web Interface
  │
  ▼
Flask Application
  │
  ▼
MySQL Database
  │
  ▼
Stored / Updated Data
  │
  ▼
Attendance Information & Reports
```

---

## ▶️ How to Run the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/jaswankumar25/Student-Attendance-Management-System.git
```

### 2. Navigate to the project folder

```bash
cd Student-Attendance-Management-System
```

### 3. Create a virtual environment

On Windows:

```bash
python -m venv venv
```

### 4. Activate the virtual environment

For Windows PowerShell:

```bash
.\venv\Scripts\Activate.ps1
```

### 5. Install the required Python packages

```bash
pip install flask mysql-connector-python
```

### 6. Configure MySQL

Create the required MySQL database and tables for the application.

Update the MySQL connection details in `app.py` according to your local MySQL configuration.

> Do not upload database passwords or other sensitive credentials to GitHub.

### 7. Run the Flask application

```bash
python app.py
```

### 8. Open the application

Open the following address in your browser:

```text
http://127.0.0.1:5000
```

---

## 🔐 Security and Git Configuration

The project contains a `.gitignore` file to prevent unnecessary and sensitive files from being uploaded to GitHub.

The following are excluded:

```text
venv/
.venv/
__pycache__/
.env
.vscode/
```

This keeps the repository clean and prevents local environment files from being committed.

---

## 📚 DBMS Concepts Demonstrated

This project demonstrates practical DBMS concepts including:

- Database creation and management
- Table creation
- Primary keys
- Data insertion
- Data retrieval
- Data updating
- Data deletion
- Database connectivity
- SQL queries
- CRUD operations
- Application–database integration

---

## 🎓 Academic Purpose

This project was developed as part of a **Database Management System (DBMS)** academic project.

It demonstrates how database concepts can be integrated with a web application to create a practical real-world solution for student attendance management.

---

## 🚀 Future Enhancements

Possible future improvements include:

- User authentication and login
- Role-based access for administrators and faculty
- Export attendance reports as PDF or Excel
- Advanced attendance analytics
- Email notifications
- Cloud database deployment
- Online hosting of the complete application
- Improved reporting and visualization

---

## 👨‍💻 Developer

**JASWAN KUMAR K**

B.Tech – Information Technology  
Specialization: Cloud Computing

---

## 📄 License

This project is developed for academic and educational purposes.