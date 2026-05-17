class Herbivore:
    def __init__(self, plant_type):
        self.plant_type = plant_type

    def forage(self):
        print(f"Foraging for {self.plant_type}.")

class Carnivore:
    def __init__(self, meat_type):
        self.meat_type = meat_type

    def hunt(self):
        print(f"Hunting for {self.meat_type}.")

# Omnivore inherits from BOTH Herbivore and Carnivore
class Omnivore(Herbivore, Carnivore):
    def __init__(self, name, plant_type, meat_type):
        self.name = name
        # Explicitly calling the constructors of both parent classes
        Herbivore.__init__(self, plant_type)
        Carnivore.__init__(self, meat_type)

    def display_diet(self):
        print(f"{self.name} is an omnivore. Watch it eat:")
        self.forage()
        self.hunt()

# --- Testing Q9 ---
print("\n--- Q9 Output ---")
bear = Omnivore("Grizzly Bear", "berries", "salmon")
bear.display_diet()