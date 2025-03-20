import mysql.connector
from contextlib import  contextmanager

@contextmanager
def get_db_cursor(commit=False):
    connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "root",
        database = "expense_manager"

    )
    if connection.is_connected():
        print("Connection Successful")
    else:
        print("Connection Failed")

    cursor = connection.cursor(dictionary=True)
    yield cursor
    if commit:
        connection.commit()

    cursor.close()
    connection.close()

def fetch_records():
    with get_db_cursor() as cursor:
        cursor.execute("SELECT * FROM expense_manager.expenses")
        expenses = cursor.fetchall()
        for expense in expenses:
            print(expense)


def fetch_expenses_for_date(expense_date):
    with get_db_cursor() as cursor:
        cursor.execute("SELECT * FROM expenses where expense_date=%s", (expense_date,))
        expenses = cursor.fetchall()
        return expenses

def insert_expense(expense_date,amount,category,notes):
    with get_db_cursor(commit=True) as cursor:
        cursor.execute(
            "Insert into expenses(expense_date,amount,category,notes) values (%s,%s,%s,%s)",(expense_date,amount,category,notes))

def delete_expense_date(expense_date):
    with get_db_cursor(commit=True) as cursor:
        cursor.execute(
            "Delete from expenses where expense_date = %s",(expense_date,))

def fetch_expense_summary(start_date,end_date):
    with get_db_cursor() as cursor:
        cursor.execute(
            "SELECT category, SUM(amount) as Total FROM expenses where expense_date between %s and %s group by category",(start_date,end_date))
        data = cursor.fetchall()
        return data


if __name__ == "__main__":
    #fetch_records()
    #insert_expense("2024-08-25",40,"Food","Samosa")
    #expenses = fetch_expenses_for_date("2024-08-25")
    #print(expenses)
    #delete_expense_date("2024-08-25")
    #fetch_records_date("2024-08-20")
    summary = fetch_expense_summary("2024-08-01", "2024-08-05")
    for record in summary:
        print(record)
