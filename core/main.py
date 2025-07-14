#main program file

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
import functions

#initialise empty data list, and csv file path to write data
userData = []
csv_file = 'data\smartspendee.csv'

#user menu
print("\nHello user, welcome to smartspendee!\n")

while True:
    print("1. Add monthly income/allowance")
    print("2. Add or edit an expense")
    print("3. View expenses")
    print("4. View statistics (Total Expenses)")
    print("5. Exit")
    
    try:
        choice = int(input("\nPlease select an option (1-5): "))
    except ValueError:
        print("Invalid input, please select options 1-5.")
        continue

    if choice == 1:
        income = float(input("\nAdd monthly income/allowance: ")) #to be used for budgeting statistics
        print(f"Logged ${income:.2f} monthly income!\n")

    elif choice == 2:
        functions.addEditExpense()

    elif choice == 3:
        readFile = pd.read_csv(csv_file)
        print("Displaying all expenses... \n", readFile)

    elif choice == 4:
        functions.totalExpenses()

    elif choice == 5:
        print("Exiting the application. Goodbye!")
        break

    else:
        print("Invalid option, please try again.")