#!/usr/bin/python3
"""izah"""


def write_file(filename="", text=""):
    """izah"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
