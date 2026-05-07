def digits(num):
    count = 0
    while num > 0:
        count = count + 1
        num = num // 10
    return count

n = int(input("Enter a positive integer : "))

print(f"The no of digits in the input number is = {digits(n)}")
