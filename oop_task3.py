'''In this task, we will create an abstract base class called "Animal" that
defines a common interface for all animals.'''
from abc import ABC, abstractmethod


class Animal(ABC):
    """The animal class is an abstract base class that
    defines a common interface for all animals.
    It includes an abstract method make_sound that
    must be implemented by all derived classes."""

    @abstractmethod
    def make_sound(self):
        """The make_sound method is an abstract method that
        must be implemented by all derived classes.
        It should return a string representing the sound made by the animal."""

    def print_name(self):
        """The print_name method is a concrete method that
        prints the name of the animal. It can be used by all derived classes."""


class Dog(Animal):
    """The dog class is a derived class that inherits from the animal class."""

    def make_sound(self):
        """The make_sound method is implemented to return the sound made by a dog."""
        return "Woof"

    def print_name(self):
        """The print_name method is implemented to return the name of the dog."""
        return "Bobby"

class Cat(Animal):
    """The cat class is a derived class that inherits from the animal class."""

    def make_sound(self):
        """The make_sound method is implemented to return the sound made by a cat."""
        return "Meow"
    def print_name(self):
        """The print_name method is implemented to return the name of the cat."""
        return "Kitty"


dog = Dog()
cat = Cat()
print(dog.make_sound())
print(cat.make_sound())
print(dog.print_name())
print(cat.print_name())
