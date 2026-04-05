# 7. Instance Methods

class Laptop:
    storage_type = "SSD"

    def __init__(self, RAM, storage):
        self.RAM = RAM
        self.storage = storage
    def get_info(self): # Instance Methods
        print(f"----- Laptop Details -----\nStorage Type: {self.storage_type}\nRAM: {self.RAM}\nStorage: {self.storage}")

lap1 = Laptop("16GB", "512GB")
lap2 = Laptop("8GB", "256GB")

lap1.get_info()
lap2.get_info()
