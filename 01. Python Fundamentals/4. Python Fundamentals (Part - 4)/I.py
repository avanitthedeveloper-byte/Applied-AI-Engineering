# 9. Static Methods

class Laptop:
    storage_type = "SSD"

    def __init__(self, RAM, storage):
        self.RAM = RAM
        self.storage = storage
    def get_info(self): # Instance Methods
        print(f"----- Laptop Details -----\nStorage Type: {self.storage_type}\nRAM: {self.RAM}\nStorage: {self.storage}")
    def get_storage_type(cls):
        print(f"----- Laptop Details -----\nStorage Type: {cls.storage_type}")
    @classmethod
    def change_storage_type(cls, name):
        cls.storage_type = name
        print(cls.storage_type)
    @staticmethod
    def cal_discount(price, discount):
        final_price = price - price*discount
        print(f"Final Discount: {final_price}")

lap1 = Laptop("16GB", "512GB")
lap2 = Laptop("8GB", "256GB")

lap1.get_storage_type()
Laptop.change_storage_type("HDD")

Laptop.cal_discount(40000, 0.10)