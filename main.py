import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

#initialise empty data list, and csv file path to write data
userData = []
csv_file = 'smartspendee.csv'

#user menu
print("Hello user, welcome to smartspendee!")

while True:
    print("1. Add a new expense")
    print("2. View expenses")
    print("3. Exit")
    
    choice = input("Please select an option (1-3): ")

    if choice == '1':
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

    elif choice == '2':
        readFile = pd.read_csv(csv_file)
        print("Displaying all expenses... \n", readFile)

    elif choice == '3':
        print("Exiting the application. Goodbye!")
        break

    else:
        print("Invalid option, please try again.")