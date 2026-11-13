# Payroll Management System

## Project Description
The Payroll Management System is a console-based application developed using Python and MySQL. It helps manage employee payroll by maintaining employee details, recording monthly attendance, and calculating net salaries based on basic salary, allowances, and deductions.

## Features

- **Employee Management:** Check existing employees and register new employee details.
- **Payroll Processing:** Generate payroll records for a selected employee and month.
- **Attendance Management:** Record total working days and present days for each payroll month.
- **Salary Calculation:** Calculate net salary using basic salary, allowances, and deductions.
- **Duplicate Payroll Prevention:** Prevent multiple payroll records for the same employee and month.
- **View Payroll:** Display employee details, attendance month, salary components, and net salary.

## Technologies Used
- Python
- MySQL
- MySQL Connector/Python
- python-dotenv

## Project Structure
```text
payroll-management-system/
│
├── main.py
├── payroll_db.sql
├── requirements.txt
├── .env.example
└── README.md
```

## Database Structure
The application uses MySQL with three main tables:

- **Employees:** Stores employee ID, employee name, and department.
- **Attendance:** Stores employee attendance details for each payroll month.
- **Salary:** Stores basic salary, allowance, and deduction details.

## Net Salary Calculation

Net Salary = Basic Salary + Allowance - Deduction

## Installation and Setup

1. Navigate to the project folder:
   ```bash
   cd payroll-management-system
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Execute the SQL file in MySQL to create the database and tables.

4. Create a `.env` file using `.env.example` and configure your MySQL credentials.

5. Run the application:
   ```bash
   python main.py
   ```

## Learning Outcomes
- Connecting Python applications with MySQL.
- Performing database operations using SQL queries.
- Working with related tables and SQL joins.
- Implementing payroll calculations.
- Validating employee attendance and salary inputs.
- Preventing duplicate monthly payroll records.