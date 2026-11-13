import mysql.connector;
import os
from dotenv import load_dotenv

load_dotenv()

#function to create connection
def create_connection():
    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )
        return connection

    except mysql.connector.Error as error:
        print("database connection error:", error)
        return None


# function to calculate net salary
def payroll():
    connection = create_connection()
    cursor = connection.cursor()

    employee_id = int(input("Enter employee id: "))
    payroll_month = input("Enter payroll month (YYYY-MM): ")

    # Check whether employee already exists
    cursor.execute(
        "SELECT employee_name, department FROM employees WHERE employee_id = %s",
        (employee_id,)
    )
    employee = cursor.fetchone()

    if employee:
        employee_name = employee[0]
        department = employee[1]
        print("Employee already exists.")
        print("Employee name:", employee_name)
        print("Department:", department)

    else:
        employee_name = input("Enter employee name: ")
        department = input("Enter department: ")

        cursor.execute(
            "INSERT INTO employees (employee_id, employee_name, department) "
            "VALUES (%s, %s, %s)",
            (employee_id, employee_name, department)
        )

    # Check whether payroll already exists for this employee and month
    cursor.execute(
        "SELECT salary_id FROM salary "
        "WHERE employee_id = %s AND payroll_month = %s",
        (employee_id, payroll_month)
    )

    existing_payroll = cursor.fetchone()

    if existing_payroll:
        print("Payroll already exists for this employee and month.")
        cursor.close()
        connection.close()
        return

    total_working_days = int(input("Enter total working days: "))
    present_days = int(input("Enter present days: "))

    if present_days > total_working_days:
        print("Present days cannot be greater than total working days.")

    else:
        basic_salary = int(input("Enter basic salary: "))
        allowance = int(input("Enter allowance: "))
        deduction = int(input("Enter deduction: "))

        if basic_salary < 0 or allowance < 0 or deduction < 0:
            print("Salary values cannot be negative.")

        else:
            # Insert attendance
            cursor.execute(
                "INSERT INTO attendance "
                "(employee_id, payroll_month, total_working_days, present_days) "
                "VALUES (%s, %s, %s, %s)",
                (employee_id, payroll_month,
                 total_working_days, present_days)
            )

            # Insert salary
            cursor.execute(
                "INSERT INTO salary "
                "(employee_id, payroll_month, basic_salary, allowance, deduction) "
                "VALUES (%s, %s, %s, %s, %s)",
                (employee_id, payroll_month,
                 basic_salary, allowance, deduction)
            )

            connection.commit()

            net = basic_salary + allowance - deduction

            print("\n--------- NET SALARY ---------")
            print("Employee ID:", employee_id)
            print("Employee Name:", employee_name)
            print("Department:", department)
            print("Payroll Month:", payroll_month)
            print("Net Salary:", net)

    cursor.close()
    connection.close()


# function to view payroll
def view_payroll():
    connection = create_connection()
    cursor = connection.cursor()

    query = """
    SELECT
        e.employee_id,
        e.employee_name,
        e.department,
        a.payroll_month,
        s.basic_salary,
        s.allowance,
        s.deduction,
        s.basic_salary + s.allowance - s.deduction AS net_salary
    FROM employees e
    JOIN attendance a
        ON e.employee_id = a.employee_id
    JOIN salary s
        ON e.employee_id = s.employee_id
        AND a.payroll_month = s.payroll_month
    """

    cursor.execute(query)
    records = cursor.fetchall()

    if records:
        for record in records:
            print("\n-------------------------------")
            print("Employee ID:", record[0])
            print("Employee Name:", record[1])
            print("Department:", record[2])
            print("Payroll Month:", record[3])
            print("Basic Salary:", record[4])
            print("Allowance:", record[5])
            print("Deduction:", record[6])
            print("Net Salary:", record[7])
            print("-------------------------------")

    else:
        print("No payroll records found.")

    cursor.close()
    connection.close()

#funtion to view payroll  
def view_payroll():
    connection=create_connection()
    cursor=connection.cursor()
    query="""select e.employee_id,e.employee_name,e.department,
    a.payroll_month,
    s.basic_salary,s.allowance,s.deduction,
    s.basic_salary+s.allowance-s.deduction as net_salary
    from employees e
    join attendance a
    on e.employee_id=a.employee_id
    join salary s
    on e.employee_id=s.employee_id
    and a.payroll_month=s.payroll_month"""   
    cursor.execute(query)
    records=cursor.fetchall()
    if records:
        for record in records:
            print("\n-------------------------------")
            print("employee_id:",record[0])
            print("employee_name:",record[1])
            print("department:",record[2])
            print("payroll_month:",record[3])
            print("basic salary:",record[4])
            print("allowance:",record[5])
            print("deduction:",record[6])
            print("net salary:",record[7])
            print("--------------------------------")
    else:
        print("no payroll records found.") 
    cursor.close()
    connection.close()     

#menu
while True:
    print("\n==========PAYROLL MANAGEMENT SYSTEM=========")
    print("1.calculate net salary")
    print("2.view payroll")
    print("3.exit")
    print("=============================================")
    choice=input("enter your choice:")
    if choice=="1":
        payroll()
    elif choice=="2":
        view_payroll()
    elif choice=="3":
        print("exit.")
        break
    else:
        print("invalid choice!")

