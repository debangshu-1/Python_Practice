class Player:
    # Class variable: shared across all instances
    player_count = 0

    def __init__(self, name, level):
        # Instance variables: unique to each instance
        self.name = name
        self.level = level
        
        # Increment the class variable whenever a new player is instantiated
        Player.player_count += 1

    def display_stats(self):
        print(f"Player: {self.name} | Level: {self.level}")

# --- Testing Q8 ---
print("\n--- Q8 Output ---")
player1 = Player("Arthur", 10)
player2 = Player("Merlin", 15)
player3 = Player("Lancelot", 12)

player1.display_stats()
player2.display_stats()
player3.display_stats()

print(f"Total players created: {Player.player_count}")