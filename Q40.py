from datetime import datetime

class Message:
    """Represents a single message sent in a chatroom."""
    def __init__(self, sender, content):
        self.sender = sender
        self.content = content
        # Automatically generate a timestamp when the message is created
        self.timestamp = datetime.now().strftime("%H:%M:%S")

    def __str__(self):
        # Defines how the message looks when printed
        return f"[{self.timestamp}] {self.sender.name}: {self.content}"

class User:
    """Represents a user who can interact with chatrooms."""
    def __init__(self, name):
        self.name = name

    def join_room(self, chat_room):
        chat_room.add_user(self)

    def leave_room(self, chat_room):
        chat_room.remove_user(self)

    def send_message(self, chat_room, content):
        # Create a new Message object and send it to the room
        message = Message(self, content)
        chat_room.receive_message(message)

class ChatRoom:
    """Manages users and the history of messages."""
    def __init__(self, name):
        self.name = name
        self.users = []    # List to hold User objects
        self.history = []  # List to hold Message objects

    def add_user(self, user):
        if user not in self.users:
            self.users.append(user)
            print(f"📢 *** {user.name} joined '{self.name}' ***")

    def remove_user(self, user):
        if user in self.users:
            self.users.remove(user)
            print(f"📢 *** {user.name} left '{self.name}' ***")

    def receive_message(self, message):
        # Only allow messages if the sender is currently in the room
        if message.sender in self.users:
            self.history.append(message)
            print(message) # Echo the message live to the console
        else:
            print(f"❌ Error: {message.sender.name} must join '{self.name}' before sending a message.")

    def view_chat_history(self):
        print(f"\n--- 📜 Chat History for '{self.name}' ---")
        if not self.history:
            print("No messages yet.")
        for msg in self.history:
            print(msg)
        print("---------------------------------------\n")


# ==========================================
# Example Usage
# ==========================================
if __name__ == "__main__":
    # 1. Create a ChatRoom
    dev_room = ChatRoom("Developer Lounge")

    # 2. Create Users
    alice = User("Alice")
    bob = User("Bob")
    charlie = User("Charlie")

    # 3. Users join the ChatRoom
    alice.join_room(dev_room)
    bob.join_room(dev_room)

    # 4. Sending messages
    alice.send_message(dev_room, "Hey Bob, how is the OOP project going?")
    bob.send_message(dev_room, "It's going well! Just setting up the classes.")
    
    # Charlie tries to send a message without joining
    charlie.send_message(dev_room, "Can I get some help?") 
    
    # Charlie joins and then sends
    charlie.join_room(dev_room)
    charlie.send_message(dev_room, "Nevermind, figured it out.")

    # 5. User leaves the room
    bob.leave_room(dev_room)
    alice.send_message(dev_room, "See ya, Bob!")

    # 6. View the complete chat history
    dev_room.view_chat_history()