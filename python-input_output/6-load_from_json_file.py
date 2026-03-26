#!/usr/bin/python3
"""
izah
"""
import json


def load_from_json_file(filename):
    """
    izah
    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
