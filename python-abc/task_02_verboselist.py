#!/usr/bin/python3
"""Defines a VerboseList class that extends list."""


class VerboseList(list):
    """A list subclass that prints notifications on modification."""

    def append(self, item):
        """Append an item and print a notification."""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, iterable):
        """Extend the list and print a notification."""
        initial_length = len(self)
        super().extend(iterable)
        added_count = len(self) - initial_length
        print("Extended the list with [{}] items.".format(added_count))

    def remove(self, item):
        """Remove an item and print a notification."""
        if item in self:
            print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Pop an item and print a notification."""
        # Retrieve item first to print it; accessing index handles IndexError edge case
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)
