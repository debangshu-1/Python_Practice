# check whether two lists share no common elements

list1 = list(map(int, input("Enter the elements into the 1st list : ").split()))
list2 = list(map(int, input("Enter the elements into the 2nd list : ").split()))

# Convert lists to sets and find the intersection
common_elements = set(list1) & set(list2) 

# An empty set evaluates to False in Python
if not common_elements: 
    print("There are no common elements in your lists")
else:
    print(f"The elements that are common in both lists = {common_elements}")