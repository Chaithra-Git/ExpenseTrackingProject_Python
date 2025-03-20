from fastapi import FastAPI
from datetime import  date

app = FastAPI()

@app.get("/expenses/{expense_date}")
def get_expenses(expense_date: date):
    return f"Received get_expense request{date}"