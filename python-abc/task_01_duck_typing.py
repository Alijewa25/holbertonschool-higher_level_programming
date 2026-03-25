#!/usr/bin/env python3
"""
Shapes, Interfaces, and Duck Typing
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for shapes"""

    @abstractmethod
    def area(self):
        """Calculate area"""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate perimeter"""
        pass


class Circle(Shape):
    """Circle class"""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Return area of the circle"""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Return perimeter (circumference) of the circle"""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle class"""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """Return area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Return perimeter of the rectangle"""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Print area and perimeter using duck typing
    (no type checking, just calling methods)
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
