class Person:
    def __init__(self, name, age=None, address=None):
        self.name = name
        self.age = age
        self.address = address

    def display_info(self):
        info = f"Name: {self.name}"
        if self.age is not None:
            info += f", Age: {self.age}"
        if self.address is not None:
            info += f", Address: {self.address}"
        print(info)

# --- Testing Q7 ---
print("--- Q7 Output ---")
# 1. name only
p1 = Person("Alice")
p1.display_info()

# 2. name + age
p2 = Person("Bob", 25)
p2.display_info()

# 3. name + age + address
p3 = Person("Charlie", 30, "123 Main St")
p3.display_info()