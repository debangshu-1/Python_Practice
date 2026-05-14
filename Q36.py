from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name):
        self.name = name

    # Decorator to define this as an abstract method
    @abstractmethod
    def calculate_salary(self):
        pass


class Intern(Employee):
    def __init__(self, name, stipend):
        super().__init__(name)
        self.stipend = stipend

    # Providing the specific implementation for Intern
    def calculate_salary(self):
        return self.stipend


class FullTimeEmployee(Employee):
    def __init__(self, name, annual_salary):
        super().__init__(name)
        self.annual_salary = annual_salary

    # Providing the specific implementation for Full-Time Employee
    def calculate_salary(self):
        return self.annual_salary / 12  # Monthly salary


class ContractEmployee(Employee):
    def __init__(self, name, hourly_rate, hours_worked):
        super().__init__(name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    # Providing the specific implementation for Contract Employee
    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked


# --- Example Usage ---
intern = Intern("Alice", 1500)
full_time = FullTimeEmployee("Bob", 120000)
contractor = ContractEmployee("Charlie", 50, 160)

print(f"{intern.name}'s Salary: ${intern.calculate_salary()}")
print(f"{full_time.name}'s Salary: ${full_time.calculate_salary()}")
print(f"{contractor.name}'s Salary: ${contractor.calculate_salary()}")