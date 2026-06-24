# 🏫 School Management System

A terminal-based School Management System built with Python and MySQL, designed to manage students, teachers, attendance, fees, and salaries for **Kalka Public School**.

---

## 📋 Features

| # | Feature | Description |
|---|---------|-------------|
| 1 | **Add Student** | Register a new student with admission number, name, roll number, class, and address |
| 2 | **Class Attendance** | Record daily class attendance and number of absent students |
| 3 | **Add Teacher** | Register a new teacher with ID, name, subject, phone, and salary |
| 4 | **Submit Fees** | Record fee payments made by students |
| 5 | **Pay Salary** | Record salary payments made to teachers |
| 6 | **Display Class** | View all students belonging to a specific class |
| 7 | **Display Students** | View all students in the database |
| 8 | **Display Teachers** | View all teachers in the database |
| 9 | **Remove Student** | Delete a student record by class and roll number |
| 10 | **Remove Teacher** | Delete a teacher record by name and ID |

---

## 🛠️ Tech Stack

- **Language:** Python 3.x
- **Database:** MySQL
- **Connector:** `mysql-connector-python`

---

## 🗄️ Database Schema

The system uses a database named `SCHOOL_MANAGEMENT_SYS` with the following tables:

**`students`**
```
AdmNo (INT, PK) | Name (CHAR) | Rollno (INT) | Class (CHAR) | address (CHAR)
```

**`teacher`**
```
T_id (INT, PK) | TName (CHAR) | Subject (CHAR) | phone (VARCHAR) | salary (FLOAT)
```

**`cl_attendance`**
```
DATE (DATE) | sClass (CHAR) | absent (INT)
```

**`Fees`**
```
sName (CHAR) | sClass (CHAR) | srollno (INT) | sMonth (CHAR) | Amt_paid (FLOAT)
```

**`Salary`**
```
tName (CHAR) | tMonth (CHAR) | sal_paid (FLOAT)
```

---

## ⚙️ Setup & Installation

### Prerequisites

- Python 3.x installed
- MySQL Server installed and running

### 1. Install the required Python package

```bash
pip install mysql-connector-python
```

### 2. Configure MySQL

Make sure your MySQL server is running. The script connects with these default credentials:

```
Host:     localhost
User:     root
Password: 1234
```

> ⚠️ **Important:** Update the credentials in the script if your MySQL setup is different:
> ```python
> conn = a.connect(host='localhost', user='root', passwd='your_password')
> ```

### 3. Set up the database and tables

Uncomment the table creation and insertion block in the script (the section wrapped in `''' ... '''`) and run the script **once** to initialize the database. Re-comment it afterward to avoid errors on subsequent runs.

### 4. Run the application

```bash
python School_management_system.py
```

### 5. Login

The system is password protected. Enter the password when prompted:

```
Password: Abhishek
```

---

## 🚀 Usage

After logging in, you'll see the main menu:

```
................KALKA PUBLIC SCHOOL...............

        1.ADD STUDENT           2.CLASS ATTENDANCE
        3.ADD TEACHER           4.SUBMIT FEES
        5.PAY SALARY            6.DISPLAY CLASS
        7.DISPLAY STUDENTS      8.DISPLAY TEACHERS
        9.REMOVE STUDENTS       10.REMOVE TEACHERS
```

Enter the number corresponding to the task you want to perform and follow the on-screen prompts.

---

## 📁 Project Structure

```
School_management_system.py   # Main application file
README.md                     # Project documentation
```

---

## 🔮 Future Improvements

- [ ] Add password hashing for better security
- [ ] Add update/edit functionality for student and teacher records
- [ ] Display attendance reports by date or class
- [ ] Export records to CSV or PDF
- [ ] Build a GUI using Tkinter or a web interface

---

## 📄 License

This project is open-source and free to use for educational purposes.
