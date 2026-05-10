# Write a program that takes a string from the user and prints the number of spaces in the string

string = input("Enter a string : ")

count = 0

for i in string:
    if i == ' ':
        count = count + 1

print(f"No of spaces in your string = {count}")