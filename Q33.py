class Student:
    def __init__(self, name, roll_no, marks):
        # Using setters in the constructor to enforce validation from the start
        self.set_name(name)
        self.set_roll_no(roll_no)
        self.set_marks(marks)

    # Getters
    def get_name(self):
        return self._name

    def get_roll_no(self):
        return self._roll_no

    def get_marks(self):
        return self._marks

    # Setters with Validation
    def set_name(self, name):
        if isinstance(name, str) and name.strip() != "":
            self._name = name.strip()
        else:
            raise ValueError("Name cannot be empty.")

    def set_roll_no(self, roll_no):
        if isinstance(roll_no, int) and 1 <= roll_no <= 100:
            self._roll_no = roll_no
        else:
            raise ValueError("Roll number must be an integer between 1 and 100.")

    def set_marks(self, marks):
        if isinstance(marks, (int, float)) and marks >= 0:
            self._marks = marks
        else:
            raise ValueError("Marks cannot be negative.")

# Example Usage:
student1 = Student("John Doe", 45, 88.5)
print(f"Student: {student1.get_name()}, Roll No: {student1.get_roll_no()}, Marks: {student1.get_marks()}")

# This will trigger a validation error:
# student2 = Student("", 105, -10)