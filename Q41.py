# 1. Open a file in write mode "names.txt"
with open("names.txt", "w") as file:
    print("Please enter 5 names:")
    
    # 2. Write 5 names (one per line) entered by the user
    for i in range(5):
        name = input(f"Name {i+1}: ")
        file.write(name + "\n")

print("\n--- Reading from file ---")

# 3. Open the same file in read mode and print all names
with open("names.txt", "r") as file:
    names_content = file.read()
    print(names_content)