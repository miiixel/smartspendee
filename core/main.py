import os
import functions
import pandas as pd

csv_file = "data/smartspendee.csv"
os.makedirs("data", exist_ok=True)

budget = float(input("Enter your budget which you aim to stick to: "))

while True:
    print("\n1. Add monthly income/allowance")
    print("2. Add or edit an expense")
    print("3. View expenses")
    print("4. View budget statistics")
    print("5. Exit")

    try:
        choice = int(input("\nPlease select an option (1-5): "))
    except ValueError:
        print("Invalid input, please select options 1-5.")
        continue

    if choice == 1:
        income = float(input("\nAdd monthly income/allowance: "))
        print(f"Logged ${income:.2f} monthly income.\n")

    elif choice == 2:
        functions.addEditExpense(csv_file)

    elif choice == 3:
        if os.path.exists(csv_file):
            df = pd.read_csv(csv_file)
            print("Displaying all expenses... \n", df)
        else:
            print("No expenses recorded yet.")

    elif choice == 4:
        functions.viewExpenses(budget, csv_file)
        functions.groupByCategory(csv_file)

    elif choice == 5:
        print("Exiting the application. Goodbye!")
        break

    else:
        print("Invalid option, please try again.")
