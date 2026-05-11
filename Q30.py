# ask the user for a string and print - 1. all unique characters and 2. The count of all unique characters

string = input("Enter a string : ")

print(f"All unique characters = {set(string)}\nThe count of unique characters = {len(set(string))}")