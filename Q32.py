class Book:
    def __init__(self, title, author):
        """Initializes the Book with a title, author, and an empty list of reviews."""
        self.title = title
        self.author = author
        self.reviews = []

    def add_review(self, review):
        """Adds a new review to the list."""
        self.reviews.append(review)
        print(f"\n[Success] Review added to '{self.title}'.")

    def count_reviews(self):
        """Returns the total number of reviews."""
        return len(self.reviews)

    def display_reviews(self):
        """Prints all the reviews for the book."""
        print(f"\n--- Reviews for '{self.title}' by {self.author} ---")
        if not self.reviews:
            print("No reviews yet.")
        else:
            for i, review in enumerate(self.reviews, start=1):
                print(f"{i}. {review}")
        print("-" * 40)


def main():
    print("=== Welcome to the Book Review System ===")
    
    # Dynamically get the initial book setup
    title = input("Enter the book title: ")
    author = input("Enter the author's name: ")
    my_book = Book(title, author)
    
    print(f"\nExcellent! '{my_book.title}' by {my_book.author} has been set up.")

    # Start the menu-driven loop
    while True:
        print("\n" + "="*30)
        print("             MENU")
        print("="*30)
        print("1. Add a new review")
        print("2. Count total reviews")
        print("3. Display all reviews")
        print("4. Exit")
        print("="*30)

        # Get dynamic input for menu choice
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            review_text = input("Write your review: ")
            if review_text.strip():  # Check to make sure it's not empty
                my_book.add_review(review_text)
            else:
                print("\n[Error] Review cannot be empty.")
                
        elif choice == '2':
            total = my_book.count_reviews()
            print(f"\nThis book currently has {total} review(s).")
            
        elif choice == '3':
            my_book.display_reviews()
            
        elif choice == '4':
            print("\nExiting the Book Review System. Goodbye!")
            break  # This stops the while loop
            
        else:
            print("\n[Error] Invalid input. Please enter a number from 1 to 4.")

# Standard Python idiom to execute the main function
if __name__ == "__main__":
    main()