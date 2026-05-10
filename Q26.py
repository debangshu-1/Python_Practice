# create a dictionary that maps each word to its length

words = list(map(str,input("Enter the words in your list : ").split()))

dictionary = {}

for i in words:
    dictionary[i] = len(i)

print(f"Dictionary created from your list = {dictionary}")