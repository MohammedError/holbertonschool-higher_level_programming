#!/usr/bin/python3
"""
Defines a CountedIterator class that counts items as they are iterated.
"""


class CountedIterator:
    """
    Iterator that counts the number of items iterated over.
    """
    def __init__(self, some_iterable):
        """
        Initialize the iterator and counter.
        """
        self.iterator = iter(some_iterable)
        self.counter = 0

    def get_count(self):
        """
        Return the current count of iterated items.
        """
        return self.counter

    def __next__(self):
        """
        Fetch the next item and increment the counter.
        """
        item = next(self.iterator)
        self.counter += 1
        return item

    def __iter__(self):
        """
        Return the iterator object itself.
        """
        return self
