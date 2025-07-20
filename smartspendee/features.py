import pandas as pd
import os
import matplotlib.pyplot as plt

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

def getExpenses():

    csv_file = "data/smartspendee.csv"
    if not os.path.exists(csv_file) or os.path.getsize(csv_file) == 0:
        return []
    
    df = pd.read_csv(csv_file)
    return df.to_dict(orient="records")

def generate_pie_chart_by_category(output_path="static/pie_chart.png"):
    import matplotlib.pyplot as plt
    import pandas as pd
    import os

    csv_file = "data/smartspendee.csv"

    if not os.path.exists(csv_file) or os.path.getsize(csv_file) == 0:
        return False

    df = pd.read_csv(csv_file)

    category_totals = df.groupby("Category")["Amount"].sum()

    plt.figure(figsize=(6, 6))
    category_totals.plot.pie(
        autopct=lambda p: f"${p * category_totals.sum() / 100:.2f}",
        startangle=90
    )
    plt.ylabel("")  # Hide y-label
    plt.title("Expenses by Category")

    os.makedirs("static", exist_ok=True)
    plt.savefig(output_path)
    plt.close()
    return True
