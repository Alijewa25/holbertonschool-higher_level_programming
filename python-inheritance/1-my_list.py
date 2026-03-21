#!/usr/bin/python3
# 1-my_list.py
"""Defines an inherited list class MyList."""


class MyList(list):
    """Implements sorted printing for the built-in list class."""

    def __init__(self, *args):
        """print the list with very secure vay"""

        if len(args) > 1:
            raise TypeError(
                "list() takes at most 1 argument ({} given)".format(len(args))
            )
        super().__init__(*args)

    def print_sorted(self):
        """my list sorter function"""

        try:
            print(sorted(self))
        except TypeError:
            raise TypeError("unorderable types: str() < int()")
