# 11. Encapsulation

# public
'''
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

acc1 = BankAccount("Rahul Kumar", 100000)

print(f"Name: {acc1.name}\nAccount Balance: {acc1.balance}")
'''

# protected
'''
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self._balance = balance

acc1 = BankAccount("Rahul Kumar", 100000)

print(f"Name: {acc1.name}\nAccount Balance: {acc1._balance}")
'''

# private
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def get_balance(self):
        return self.__balance
    
    def set_balance(self, balance):
        self.__balance = balance

acc1 = BankAccount("Rahul Kumar", 100000)

print(f"Name: {acc1.name}\nAccount Balance: {acc1.get_balance()}")

acc1.set_balance(500000000)

print(f"Name: {acc1.name}\nAccount Balance: {acc1.get_balance()}")

# Another way to access private attribute
print(acc1._BankAccount__balance)