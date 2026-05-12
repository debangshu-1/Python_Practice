# create a bank account class with attributes account number , owner name , and balance . and methods to deposit , withdraw , and check balance .

class BankAccount :
    def __init__(self,ac_no,owner,bal):
        self.account_number = ac_no
        self.owner_name = owner
        self.balance = bal

    def deposit(self,amount):
        if amount > 0:
            self.balance = self.balance + amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self,amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print(f"Insufficient funds! Available balance: ${self.balance:.2f}")
        else:
            self.balance -= amount
            print(f"Withdrew Rs.{amount:.2f}. New balance: Rs.{self.balance:.2f}")
    def check_balance(self):
        print(f"Account '{self.account_number}' ({self.owner_name}) Balance: ${self.balance:.2f}")
        return self.balance
    
ac = int(input("Account number : "))
name = input("Owner name : ")
balance_amount = float(input("Balance : "))

account = BankAccount(ac_no = ac,owner = name,bal = balance_amount)

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