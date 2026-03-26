#!/usr/bin/python3
"""izah"""

class Student:
    """izah"""

    def __init__(self, first_name, last_name, age):
        """izah"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """izah"""
        return self.__dict__
