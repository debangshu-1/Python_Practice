# Given a list , print all elements that appear more than once in the list

list1 = list(map(str , input("Enter the elements into the list : ").split()))

s = set()
s_common = set()

for i in list1:
    if i not in s:
        s.add(i)
    else:
        s_common.add(i)

if s_common == set():
    print("There is no elements that appear in the list more than once .")
else:
    print(f"The elements that appear in the list more than once : {s_common}")