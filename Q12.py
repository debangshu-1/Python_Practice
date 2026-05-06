def Even_in_range(num1 , num2):
    for i in range(num1 , num2+1):
        if i%2 == 0:
            print(i,end=" ")
    return None

a = int(input("Enter lower bound integer : "))
b = int(input("Enter upper bound integer : "))

print(f"The even numbers between {a} and {b} = ",end="")

Even_in_range(a,b)

print("\n")