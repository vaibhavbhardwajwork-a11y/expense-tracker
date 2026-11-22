expenses = []

def add_expense(expenses):
    while True:
        expense_type = input("Enter expense type: ")
        expense_type = expense_type.strip().lower()
        if expense_type == "":
            print("Expense type cannot be empty.")
            continue
        break

    while True:
        expense_amount = input("Enter expense amount: ")
        try:
            expense_amount = float(expense_amount)
        except ValueError:
            print("Pls enter a valid amount.")
            continue
        if expense_amount <= 0:
            print("Amount must be greater than zero.")
            continue
        break

    expense_disc = input("Enter expense description: ")
    expense_disc = expense_disc.strip()


    details_expense = {"category" : expense_type,
                       "amount" : expense_amount,
                       "description" : expense_disc}
    expenses.append(details_expense)
    print("Expense added successfully.\n")

def show_menu():
    print("------Select option------")
    print("1. Add expense")
    print("2. View expenses")
    print("3. Show total")
    print("4. Quit")

while True:
    show_menu()
    option = input("Enter option number: ")
    option = option.strip()

    if option == "1":
        add_expense(expenses)



    elif option == "2":
        print("View expense selected.\n")


    elif option == "3":
        print("Show total selected.\n")


    elif option == "4":
        print("Quit selected.\n")
        break

    else:
        print("Pls enter a valid option\n")




