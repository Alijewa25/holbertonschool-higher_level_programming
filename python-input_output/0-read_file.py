#!/usr/bin/python3
"""izah"""


def read_file(filename=""):
    """izah"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
