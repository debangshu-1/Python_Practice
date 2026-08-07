'''  Create a BankAccount class with attributes account_number, owner_name, and balance, , 
Add methods to deposit, withdraw, and check balance'''

class BankAccount :
    def __init__(self, account_number, owner_name, balance) :
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self, amount) :
        if amount < 0 :
            print(f"{amount} is not a valid amount")
        elif amount == 0 :
            print(f"No change in balance due to the deposit amount is {amount} Rs.")
        else :
            self.balance += amount
            print(f"Rs. {amount} has been successfully depositted")

    def withdraw(self, amount) :
        if amount < 0 :
            print(f"{amount} is not a valid amount")
        elif amount == 0 :
            print(f"No change in balance due to the withdraw amount is {amount} Rs.")
        elif amount > self.balance :
            print(f"Insufficient balance , withdraw amount Rs. {amount} is greater than current balance")
        else :
            self.balance -= amount
            print(f"Rs. {amount} has been successfully withdrawn")

    def check_balance(self) :
        print(f"Account Number : {self.account_number}")
        print(f"Account Holder : {self.owner_name}")
        print(f"Banance : Rs. {self.balance}")

ac = int(input("Account number : "))
name = input("Owner name : ")
balance_amount = float(input("Balance : "))

account = BankAccount(ac, name, balance_amount)

while(True):
    print("-------MENU-------")
    print("Press 1 for make a deposite")
    print("Press 2 for make a withdraw")
    print("Press 3 for checking balance")
    print("Press 4 for Exit")

    choice = int(input("Enter your choice : "))

    match choice:
        case 1:
            deposit = float(input("Enter the deposite amount : "))
            account.deposit(deposit)
        case 2:
            withdraw = float(input("Enter the withdraw amount : "))
            account.withdraw(withdraw)
        case 3:
            account.check_balance()   
        case 4:
            exit(0)
        case _:
            print("Invalid choice ! Try again !")