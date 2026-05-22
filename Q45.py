try:
    # Try to open "data.txt" in read mode
    with open("data.txt", "r") as file:
        content = file.read()
        print("File contents:", content)
        
except FileNotFoundError:
    # Catch the exception if the file doesn't exist
    print("File not found!")