# 10. Practice Problem
class Product:
    total_product = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price
        Product.total_product += 1
    
    def display_product(self):
        print(f"----- Product Details -----\nProduct Name: {self.name}\nPrice: Rs.{self.price}")

    @classmethod
    def all_product(cls):
        print(f"Total Product: {cls.total_product}")
    
    @staticmethod
    def discounted_price(price, discount):
        final_price = price - price * discount/100
        print(f"Discounted Price: {final_price}")

prod1 = Product("Biscuit", 99)
prod2 = Product("Kurkure", 89)
prod3 = Product("Sprite", 34)

prod1.display_product()
prod2.display_product()
prod3.display_product()

Product.all_product()
Product.discounted_price(50000, 10)