from dog import Dog


# This module defines the big dog class.
# the big dog class extends the Dog class
# the big dog says woof woooof
class BigDog(Dog):
    # Constructor method for the dog class
    def __init__(self, type="Big Dog"):
        super().__init__(type)

    # The big dog greets by saying woof, wooof
    # This method prints woof, woooof
    def greets(self):
        super().greets()
        print("woooof")