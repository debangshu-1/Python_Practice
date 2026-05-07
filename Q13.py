def digits(num):
    while num > 0:
        print(f"{num % 10}",end=" ")
        num = num // 10
    return None

n = int(input("Enter a positive integer : "))

print("The digits in the input number are (right to left) = ",end="")
digits(n)
print("\n")