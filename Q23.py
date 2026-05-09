# merge two lists and sort them

list1 = list(map(int,input("Enter the numbers of the 1st list : ").split()))

list2 = list(map(int,input("Enter the numbers in the 2nd list : ").split()))

result = []

result = list1 + list2

result.sort()

print(f"Result list = {result}")