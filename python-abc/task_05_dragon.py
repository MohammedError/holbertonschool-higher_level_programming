#!/usr/bin/python3
"""
Defines mixins for swimming and flying, and a Dragon class that uses them.
"""


class SwimMixin:
    """Mixin class to add swimming capability."""
    def swim(self):
        """Print swimming behavior."""
        print("The creature swims!")


class FlyMixin:
    """Mixin class to add flying capability."""
    def fly(self):
        """Print flying behavior."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    A class representing a Dragon that inherits swimming and flying capabilities.
    """
    def roar(self):
        """Print roaring behavior."""
        print("The dragon roars!")
