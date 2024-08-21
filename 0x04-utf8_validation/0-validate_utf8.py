#!/usr/bin/python3
"""
validUTF8 Module
"""


def validUTF8(data: list) -> bool:
    """
        Function validUTF8 to validate the utf-8 encoding
    """
    for char in data:
        if char > 255:
            return False
    return True
