# given a tuple of integers and create a tuple of all even and all odd numbers separately

tup = tuple(map(int,input("Enter the integers : ").split()))

tup_odd = ()
list_odd = []
tup_even = ()
list_even = []

for i in tup:
    if i % 2 == 0:
        list_even.append(i)
    else:
        list_odd.append(i)

tup_odd = tuple(list_odd)
tup_even = tuple(list_even)

print(f"A tuple of all even numbers = {tup_even}")

print(f"A tuple of all odd numbers = {tup_odd}")