expenses = []

def add_expense(expenses):
    while True:
        category = input("Enter expense type: ")
        category = category.strip().lower()
        if category == "":
            print("Expense type cannot be empty.")
            continue
        break

    while True:
        amount = input("Enter expense amount: ")
        try:
            amount = float(amount)
        except ValueError:
            print("Pls enter a valid amount.")
            continue
        if amount <= 0:
            print("Amount must be greater than zero.")
            continue
        break

    description = input("Enter expense description: ")
    description = description.strip()


    details = {"category" : category,
               "amount" : amount,
               "description" : description}
    expenses.append(details)
    print("Expense added successfully.\n")

def view_expenses(expenses):
    if not expenses:
        print("No expenses yet.")
        return

    for expense in expenses:
        print(f"Expense category : {expense['category']}")
        print(f"Expense amount : {expense['amount']:.2f}")
        print(f"Expense description : {expense['description']}")
        print()

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
        view_expenses(expenses)


    elif option == "3":
        print("Show total selected.\n")


    elif option == "4":
        print("Quit selected.\n")
        break

    else:
        print("Pls enter a valid option\n")




