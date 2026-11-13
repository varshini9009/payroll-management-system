--- creating database---
create database payroll_db;

--- use database---
use payroll_db;

--- create tables---

create table employees
(employee_id int primary key,
employee_name varchar(100),
department varchar(100));

create table attendance
(attendance_id int auto_increment primary key,
employee_id int,
attendance_date date,
total_working_days int,
present_days int,
foreign key(employee_id)references employees(employee_id));
alter table attendance change attendance_date payroll_month varchar(7);

create table salary
(salary_id int auto_increment primary key,
employee_id int,
salary_date date,
basic_salary decimal(10,2),
allowance decimal(10,2),
deduction decimal(10,2),
foreign key(employee_id)references employees(employee_id));
alter table salary change salary_date payroll_month varchar(7);
select*from salary;