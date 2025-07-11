#user menu for smartspendee application

import csv

print("Welcome to smartspendee!")

csv_file: 'smartspendee.csv'


csv_file = 'smartspendee.csv'

while True:
    print("1. Add a new expense")
    print("2. View expenses")
    print("3. Exit")
    
    choice = input("Please select an option (1-3): ")
    

    #user inputs here include adding the name of the expense, the amount, and the category it belongs to
    if choice == '1':
        item = input("Enter the item: ")
        expense = input("Enter the expense details: ")
        category = input("Enter the category: ")
        with open(csv_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([item, expense, category])
        print(f"Expense '{item}' added.")
    

    #user option allows the user to view their expenses
    elif choice == '2':
        print("Displaying all expenses...")
        try:
            with open(csv_file, mode='r', newline='') as file:
                reader = csv.reader(file)
                for idx, row in enumerate(reader, start=1):
                    print(f"{idx}: {row}")
        except FileNotFoundError:
            print("No expenses found. Please add some first.")
        # Here you would normally fetch and display expenses from a database or file
    
    #exits the application
    elif choice == '3':
        print("Exiting the application. Goodbye!")
        break
    
    #invalid option handling
    else:
        print("Invalid option, please try again.")