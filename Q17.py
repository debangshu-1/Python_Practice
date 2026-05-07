while(1):
    print("Menu")
    print("Press 1 for enter a new number to check positive / negative ")
    print("Press 2 for exit from the program")
    choice = int(input("Enter your choice from the menu : "))

    if choice == 1:
        n = float(input("Enter a number = "))
        if n >= 0:
            print(f"{n} is a positive number")
        else:
            print(f"{n} is a negative number")
    elif choice == 2:
        exit(0)
    else:
        print("Invalid Choice ! Please choose from the menu !")