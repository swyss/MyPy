# Demonstrates basic object-oriented programming in Python

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce_yourself(self):
        """Introduces the person."""
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Creating instances of the Person class
alice = Person("Alice", 30)
bob = Person("Bob", 25)

# Each instance calls the introduce_yourself method
alice.introduce_yourself()
bob.introduce_yourself()
