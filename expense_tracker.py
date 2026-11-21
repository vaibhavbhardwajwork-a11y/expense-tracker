expenses = []

def add_expense(expenses):
    expense_type = input("Enter expense type: ")
    while True:
        expense_amount = input("Enter expense amount: ")
        try:
            expense_amount = float(expense_amount)
        except ValueError:
            print("Pls enter a valid amount.")
            continue
        if expense_amount < 0:
            print("Amount cannot be negaative")
            continue
        break


    details_expense = {"category" : expense_type,
                       "amount" : expense_amount}
    expenses.append(details_expense)

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
        print("Added expense succesfully.\n")


    elif option == "2":
        print("View expense selected.\n")


    elif option == "3":
        print("Show total selected.\n")


    elif option == "4":
        print("Quit selected.\n")
        break

    else:
        print("Pls enter a valid option\n")




