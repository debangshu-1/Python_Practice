'''Design & create an online store for Products(name , price)
Track total products being created
Create a static method to calculate discount on each product based on a % parameter'''

class Online_store :

    product_count = 0

    def __init__(self, name, price) :
        self.name = name
        self.price = price
        Online_store.product_count = Online_store.product_count + 1

    def show_products(self) :
        print("---Product Details---")
        print(f"Product name : {self.name}")
        print(f"Product price : {self.price}")

    @classmethod
    def get_count(cls):
        print(f"Total product in store : {cls.product_count}")

    @staticmethod
    def calculate_discount(price, discount) :
        discounted_price = price - (price * discount / 100)
        print(f"Discounted price : {discounted_price}")

p1 = Online_store("Tooth Brush", 20)
p2 = Online_store("Tooth Paste", 50)

p1.show_products()
p1.calculate_discount(20, 5)

print("\n")
p2.show_products()
p2.calculate_discount(50, 7)

print("\n")
Online_store.get_count()