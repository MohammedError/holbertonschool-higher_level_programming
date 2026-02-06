#!/usr/bin/env python3
"""
Task 1: Pickling Custom Classes
"""
import pickle


class CustomObject:
    """A custom class to demonstrate pickling."""

    def __init__(self, name, age, is_student):
        """
        Initialize the CustomObject.

        Args:
            name (str): The name of the person.
            age (int): The age of the person.
            is_student (bool): Whether the person is a student.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display the object's attributes."""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """
        Serialize the current instance to a file.

        Args:
            filename (str): The name of the file to save to.
        """
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an instance from a file.

        Args:
            filename (str): The name of the file to load from.

        Returns:
            CustomObject: The deserialized instance, or None if error.
        """
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except (FileNotFoundError, EOFError, pickle.PickleError, Exception):
            return None
