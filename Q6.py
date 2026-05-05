num1 = int(input("Enter 1st number : "))
num2 = int(input("Enter 2nd number : "))

print(f"Before Swap : 1st number = {num1} , 2nd number = {num2}")

temp = num1
num1 = num2
num2 = temp

print(f"After Swap : 1st number = {num1} , 2nd number = {num2}")