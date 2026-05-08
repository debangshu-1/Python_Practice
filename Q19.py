def isPrime(n):
    counter = 0
    if n == 0 or n == 1:
        return False
    for i in range(2,n//2):
        if n % i == 0:
            counter = counter + 1
            return False
    return True

num = int(input("Enter a +ve integer to check Prime or not : "))

if isPrime(num):
    print(f"{num} is Prime")
else:
    print(f"{num} is not prime")