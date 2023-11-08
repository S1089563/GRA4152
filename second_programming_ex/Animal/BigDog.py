from dog import Dog


# This module defines the big dog class.
# the big dog class extends the Dog class
# the big dog says woof woooof
class BigDog(Dog):
    # Constructor method for the dog class
    # This is an example of inheritance. BigDog inherits the __init__ method from the superclasses
    def __init__(self, type="Big Dog"):
        super().__init__(type)

    # The big dog greets by saying woof, wooof
    # @return This method prints woof, woooof
    # This is an example of overriding and inheritance. BigDog inherits the greets method from Dog and extends it
    def greets(self):
        super().greets()
        return print("woooof")
