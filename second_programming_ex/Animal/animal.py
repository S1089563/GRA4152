# This module defines the animal class.
# An animal can make different sounds.
class Animal:
    # Constructor method for the class
    # It receives the type of animal
    # @param type: type of animal
    def __init__(self, type):
        self._type = type

    # Abstract method of the class.
    # Each animal has a different way of greeting
    # This is a polymorphic method that depends on the specific animal
    def greets(self):
        raise NotImplementedError









