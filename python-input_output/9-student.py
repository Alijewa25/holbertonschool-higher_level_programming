#!/usr/bin/python3
"""
Student klassı üçün modul izahı.
"""


class Student:
    """Tələbəni təyin edən klass."""

    def __init__(self, first_name, last_name, age):
        """Obyekt yaradılarkən atributları mənimsədir."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Obyektin lüğət (dict) təmsilini qaytarır."""
        return self.__dict__
