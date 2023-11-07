from animal import Animal


# This module defines the cat class.
# the cat class extends the Animal class
# the cat says meow
class Cat(Animal):
    # Constructor method for the cat class
    def __init__(self, type="Cat"):
        super().__init__(type)

    # Defines the greeting of the cat
    # This method prints meow
    def greets(self):
        print("meow")
