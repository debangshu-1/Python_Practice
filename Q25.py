'''
Create a dictionary where:
•Keys = student names
•Values = marks (integer)
Write a menu - based program where user presses a key(ʼAʼ,‘Bʼ,‘Cʼ,‘Dʼ) depending on the operation they want to perform on the dictionary:
1.A -Add a student 
2.B -Update marks 
3.C -Search for a student 
4.D -Display all students and marks
'''

def student_management_system():
    # Initialize an empty dictionary to store student data
    students = {}

    while True:
        # Display the menu options
        print("\n=== Student Menu ===")
        print("A - Add a student")
        print("B - Update marks")
        print("C - Search for a student")
        print("D - Display all students and marks")
        print("E - Exit program")
        
        # Get user input and convert to uppercase to handle 'a' or 'A'
        choice = input("Enter your choice (A/B/C/D/E): ").strip().upper()

        if choice == 'A':
            name = input("Enter the student's name: ").strip()
            if name in students:
                print("Student already exists. Please use option 'B' to update their marks.")
            else:
                try:
                    marks = int(input(f"Enter the marks for {name}: "))
                    students[name] = marks
                    print(f"Successfully added {name} to the database.")
                except ValueError:
                    print("Error: Marks must be a valid integer.")

        elif choice == 'B':
            name = input("Enter the student's name to update: ").strip()
            if name in students:
                try:
                    new_marks = int(input(f"Enter the new marks for {name}: "))
                    students[name] = new_marks
                    print(f"Successfully updated {name}'s marks to {new_marks}.")
                except ValueError:
                    print("Error: Marks must be a valid integer.")
            else:
                print(f"Student '{name}' not found. Please add them first using option 'A'.")

        elif choice == 'C':
            name = input("Enter the student's name to search: ").strip()
            if name in students:
                print(f"Result: {name} scored {students[name]} marks.")
            else:
                print(f"Student '{name}' not found.")

        elif choice == 'D':
            if not students:
                print("The database is currently empty. No students to display.")
            else:
                print("\n--- Student Records ---")
                for name, marks in students.items():
                    print(f"Name: {name} | Marks: {marks}")
                print("-----------------------")

        elif choice == 'E':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice! Please select a valid option from the menu.")

# Run the program
if __name__ == "__main__":
    student_management_system()