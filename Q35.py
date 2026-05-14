class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        return f"Brand: {self.brand}, Model: {self.model}"


class Car(Vehicle):
    def __init__(self, brand, model, seats):
        # Call the __init__ method of the parent class (Vehicle)
        super().__init__(brand, model)
        self.seats = seats

    def display_car_info(self):
        return f"{self.display_info()}, Seats: {self.seats}"


class Bike(Vehicle):
    def __init__(self, brand, model, engine_cc):
        # Call the __init__ method of the parent class (Vehicle)
        super().__init__(brand, model)
        self.engine_cc = engine_cc

    def display_bike_info(self):
        return f"{self.display_info()}, Engine: {self.engine_cc}cc"


# --- Example Usage ---
my_car = Car("Toyota", "Camry", 5)
my_bike = Bike("Yamaha", "MT-07", 689)

print(my_car.display_car_info())
print(my_bike.display_bike_info())