

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
        print("Add expense selected.\n")


    elif option == "2":
        print("View expense selected.\n")


    elif option == "3":
        print("Show total selected.\n")


    elif option == "4":
        print("Quit selected.\n")
        break

    else:
        print("Pls enter a valid option\n")




