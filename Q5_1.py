file = open("names.txt","w")

for i in range(5) :
    file.write(input("Name : ") + "\n")

file.close()

with open("names.txt","r") as file :
    print(file.read())