import pandas as pd
import os
import matplotlib.pyplot as plt

def addEditExpense(csv_file):
    while True:
        print("\n1. Add an expense\n2. Edit (delete) an expense\n3. Exit")
        try:
            option = int(input("Select an option: "))
        except ValueError:
            print("Please enter a valid option.")
            continue

        if option == 1:
            item = input("Enter the item: ")
            try:
                expense = float(input("Enter the expense details: "))
            except ValueError:
                print("Invalid number for expense.")
                continue
            category = input("Enter the category: ")

            record = {
                "Item": item,
                "Expense": expense,
                "Category": category
            }

            df = pd.DataFrame([record])
            df.to_csv(csv_file, mode='a', header=not os.path.exists(csv_file), index=False)
            print(f"✅ Saved to {os.path.abspath(csv_file)}")
            print("📄 Preview of file content:")
            print(pd.read_csv(csv_file).tail())
            print(f"Saved expense: {record}")

        elif option == 2:
            if os.path.exists(csv_file) and os.path.getsize(csv_file) > 0:
                df = pd.read_csv(csv_file)
                print("\nCurrent Expenses:")
                print(df.to_string(index=True))

                try:
                    rowIndex = int(input("Enter the row number to delete: "))
                    if 0 <= rowIndex < len(df):
                        df = df.drop(index=rowIndex).reset_index(drop=True)
                        df.to_csv(csv_file, index=False)
                        print("Expense deleted successfully.")
                    else:
                        print("Invalid row number.")
                except ValueError:
                    print("Please enter a valid row number.")
            else:
                print("No expenses recorded yet.")

        elif option == 3:
            print("Exiting the expense editor.")
            break

        else:
            print("Invalid option, please try again.")


def viewExpenses(budget, csv_file):
    if os.path.exists(csv_file) and os.path.getsize(csv_file) > 0:
        df = pd.read_csv(csv_file)
        totalExpenses = df["Expense"].sum()
        print(f"Total expenses this month is ${totalExpenses:.2f}")  # total expenses
        remainingExpenses = budget - totalExpenses
        print(f"Remaining expenses for the month is {remainingExpenses:.2f}")  # remaining expenses
    else:
        print("No expense data to summarise")


def groupByCategory(csv_file):
    if os.path.exists(csv_file) and os.path.getsize(csv_file) > 0:
        df = pd.read_csv(csv_file)
        df["Category"] = df["Category"].str.strip().str.lower()
        category_totals = df.groupby("Category")["Expense"].sum().sort_values(ascending=False)

        print("\nExpense Breakdown by Category:")
        print(category_totals.to_string())

        # Optional: show pie chart
        category_totals.plot.pie(
            autopct="%1.1f%%", figsize=(6, 6), title="Expenses by Category"
        )
        plt.ylabel("")
        plt.tight_layout()
        plt.show()

    else:
        print("No expenses recorded yet.")
