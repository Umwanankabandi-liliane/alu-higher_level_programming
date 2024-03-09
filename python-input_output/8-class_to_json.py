#!/usr/bin/python3

"""Defines a Python class-to-JSON function."""


def class_to_json(obj):
    """Return the dictionary representationof a simple data structures."""
    return obj.__dict__
