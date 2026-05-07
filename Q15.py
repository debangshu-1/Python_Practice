def digits(num):
    summ = 0
    while num > 0:
        summ = summ + (num % 10)
        num = num // 10
    return summ

n = int(input("Enter a positive integer : "))

print(f"The sum of the digits in the input number is = {digits(n)}")