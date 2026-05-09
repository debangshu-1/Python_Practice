# check if a string is palindrome or not

string = input("Enter your input string to check if it's a palindrome or not : ")

for i in range(len(string)):
    if string[i] != string[-(i+1)]:
        print(f"{string} is not a palindrome")
        exit(0)
    else:
        continue
print(f"{string} is a Palindrome")