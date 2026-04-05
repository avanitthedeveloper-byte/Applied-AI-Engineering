# 14. Abstraction

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Lion(Animal):
    def make_sound(self):
        print("Roar!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

l1 = Lion()
l1.make_sound()

c1 = Cat()
c1.make_sound()