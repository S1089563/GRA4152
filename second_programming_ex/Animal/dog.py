from animal import Animal


# This module defines the dog class.
# the dog class extends the Animal class
# the dog says wooof
class Dog(Animal):
    # Constructor method for the dog class
    # @param type: type of dog
    def __init__(self, type="Dog"):
        super().__init__(type)

    # Overrides the Animal greets() method
    # Defines the greeting of the dog
    # This method prints woof
    def greets(self):
        print("woof")
