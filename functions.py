#functions stay in this file to neaten main program code

import pandas as pd
import os
userData = []
csv_file = 'smartspendee.csv'


def addEditExpense():
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
            df.to_csv(csv_file, mode ='a', header=not os.path.exists(csv_file), index=False)

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
            print("Exiting the application. Goodbye!")
            break

        else:
            print("Invalid option, please try again.")

def totalExpenses():
    if os.path.exists(csv_file) and os.path.getsize(csv_file) > 0:
        df = pd.read_csv(csv_file)
        totalExpenses = df["Expense"].sum()
        print(f"Total expenses this month is ${totalExpenses:.2f}")
    
    else:
        print("No expense data to summarise")

if __name__ == "__main__":
    addEditExpense()
    totalExpenses()


