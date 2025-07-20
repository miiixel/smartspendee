import pandas as pd
import os

os.makedirs("data", exist_ok=True)

def saveIncome(income):
	os.makedirs("data", exist_ok=True)
	record = {
		"Income": float(income)
	}

	csv_file = "data/income.csv"
	df=pd.DataFrame([record])
	df.to_csv(csv_file, mode='a', header=not os.path.exists(csv_file), index=False)

def addExpense(item, amount, category, csv_file="data/smartspendee.csv"):
    os.makedirs("data", exist_ok=True)
    record = {
        "Item": item,
        "Amount": float(amount),
        "Category": category
    }
    df = pd.DataFrame([record])
    header = not os.path.exists(csv_file) or os.path.getsize(csv_file) == 0
    df.to_csv(csv_file, mode='a', header=header, index=False)