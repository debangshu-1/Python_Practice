# compute the average of all numbers in the list

lst = list(map(float,input("Enter the numbers one by one : ").split()))

average = 0

for i in range(len(lst)):
    average = average + lst[i]

average = average / len(lst)

print(f"Average of all the numbers in the list = {average : .2f}")