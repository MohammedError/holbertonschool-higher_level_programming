#!/usr/bin/python3
"""
Defines classes for Fish, Bird, and FlyingFish to demonstrate multiple inheritance.
"""


class Fish:
    """A class representing a fish."""
    def swim(self):
        """Print the fish swimming behavior."""
        print("The fish is swimming")

    def habitat(self):
        """Print the fish habitat."""
        print("The fish lives in water")


class Bird:
    """A class representing a bird."""
    def fly(self):
        """Print the bird flying behavior."""
        print("The bird is flying")

    def habitat(self):
        """Print the bird habitat."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    A class representing a flying fish that inherits from both Fish and Bird.
    """
    def fly(self):
        """Override fly behavior."""
        print("The flying fish is soaring!")

    def swim(self):
        """Override swim behavior."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Override habitat behavior."""
        print("The flying fish lives both in water and the sky!")
