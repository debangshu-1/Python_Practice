import json

# Create the initial dictionary of 3 cities and their populations
cities_data = {
    "Tokyo": 37400068,
    "Delhi": 29399141,
    "Shanghai": 26317104
}

# Save it to "cities.json"
with open("cities.json", "w") as file:
    json.dump(cities_data, file, indent=4)

# 1. Load the JSON and print each city and its population
with open("cities.json", "r") as file:
    loaded_cities = json.load(file)

print("Current Cities and Populations:")
for city, population in loaded_cities.items():
    print(f"- {city}: {population:,}")

# 2. Ask the user for a new city & its population
new_city = input("\nEnter a new city name: ")
new_population = int(input(f"Enter the population for {new_city}: "))

# Update the dictionary with the new info
loaded_cities[new_city] = new_population

# Save the updated dictionary back to the JSON file
with open("cities.json", "w") as file:
    json.dump(loaded_cities, file, indent=4)

print(f"\nSuccess! {new_city} has been added to cities.json.")