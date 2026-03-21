#!/usr/bin/python3
"""This module defines a Rectangle class with width and height attributes."""

class Rectangle:
    """Rectangle class with width and height attributes."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle instance.

        Args:
            width (int): Width of the rectangle (default 0).
            height (int): Height of the rectangle (default 0).
        """
        self.width = width
        self.height = height

    @property
    def dict_(self):
        """Return the rectangle attributes as a dictionary."""
        return {"width": self.width, "height": self.height}
