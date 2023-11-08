from animal import Animal


# This module defines the dog class.
# the dog class extends the Animal class
# the dog says wooof
class Dog(Animal):
    # Constructor method for the dog class
    # @param type: type of dog
    # This is an example of inheritance. Dog inherits the __init__ method from Animal
    def __init__(self, type="Dog"):
        super().__init__(type)

    # Overrides the Animal greets() method
    # Defines the greeting of the dog
    # @return This method prints woof
    # This is an example of overriding. Dog inherits the greets method from Animal and extends it
    def greets(self):
        return print("woof")
