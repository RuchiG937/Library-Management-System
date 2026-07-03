# 📚 Library Management System

A **Library Management System** developed using **Python, SQLite, Object-Oriented Programming (OOP), and Streamlit**. The application provides an interactive web interface for managing students, books, issuing and returning books, while maintaining library records efficiently.

---

## 🚀 Features

### 👨‍🎓 Student Management

* Import students from CSV
* View all students
* Search students by Student ID

### 📚 Book Management

* Import books from CSV
* Add new books
* Increase book quantity
* View all books
* Search books by Book ID

### 📖 Library Operations

* Issue books to students
* Return books
* Automatic due date calculation (15 days)
* Automatic fine calculation for late returns
* Prevent duplicate book issue
* Prevent issuing books to students with overdue books
* Automatic quantity management

### 📊 Dashboard

* Total Students
* Total Book Titles
* Available Book Copies
* Issued Books

---

## 🛠️ Technologies Used

* Python
* Streamlit
* SQLite
* Pandas
* Object-Oriented Programming (OOP)

---

## 📂 Project Structure

```text
Library_Management_System/

│
├── app.py
├── database.py
├── student.py
├── book.py
├── library_manager.py
│
├── pages/
│   ├── home.py
│   ├── dashboard.py
│   ├── students.py
│   ├── books.py
│   ├── issue_book.py
│   └── return_book.py
│
├── students.csv
├── books.csv
├── library.db
└── README.md
```

---


## 📷 Application Modules

* 🏠 Home
* 📊 Dashboard
* 👨‍🎓 Student Management
* 📚 Book Management
* 📖 Issue Book
* ↩️ Return Book

---

## 💡 Future Improvements

* User Authentication
* Barcode/QR Code Support
* Email Due Date Notifications
* Export Reports (PDF/Excel)
* Book Reservation System
* Admin Dashboard
* Pagination and Advanced Search

---

## 👩‍💻 Developer

**Ruchi**

B.Tech CSE (AI & DS)

Built using Python, SQLite, Streamlit, and Object-Oriented Programming.
