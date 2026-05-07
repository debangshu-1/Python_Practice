def calculator(a,b,operation):
    if operation == "+":
        return a+b
    elif operation == "-":
        return a-b
    elif operation == "*":
        return a*b
    elif operation == "/":
        return a/b
    else:
        return None
    
while(1):

    print("MENU")
    print("Press 1 for addition")
    print("Press 2 for subtraction")
    print("Press 3 for multiplication")
    print("Press 4 for division")
    print("Press 5 for Exit from the program")

    choice = int(input("Enter the choice from menu = "))

    match choice:
        case 1:
            num1 = float(input("Enter 1st number = "))
            num2 = float(input("Enter 2nd number = "))
            print(f"{num1} + {num2} = {calculator(num1,num2,"+")}")
        case 2:
            num1 = float(input("Enter 1st number = "))
            num2 = float(input("Enter 2nd number = "))
            print(f"{num1} - {num2} = {calculator(num1,num2,"-") : .2f}")
        case 3:
            num1 = float(input("Enter 1st number = "))
            num2 = float(input("Enter 2nd number = "))
            print(f"{num1} * {num2} = {calculator(num1,num2,"*")}")
        case 4:
            num1 = float(input("Enter 1st number = "))
            num2 = float(input("Enter 2nd number = "))
            print(f"{num1} / {num2} = {calculator(num1,num2,"/") : .2f}")
        case 5:
            exit(0)
        case _:
            print("INVALID CHOICE !")