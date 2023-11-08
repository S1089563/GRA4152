from animal import Animal


# This module defines the cat class.
# the cat class extends the Animal class
# the cat says meow
class Cat(Animal):
    # Constructor method for the cat class
    # This is an example of inheritance. Cat inherits the __init__ method from Animal
    def __init__(self, type="Cat"):
        super().__init__(type)

    # Defines the greeting of the cat
    # @return This method prints meow
    # This is an example of overriding. Cat inherits the greets method from Animal and extends it
    def greets(self):
        return print("meow")
