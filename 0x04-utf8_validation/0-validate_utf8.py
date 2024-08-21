#!/usr/bin/python3
"""
validUTF8 Module
"""


def validUTF8(data: list) -> bool:
    """
        Function validUTF8 to validate the utf-8 encoding
    """
    for byte in data:
        if byte < 0x00 or byte > 0xFF:
            return False
        
    # If all bytes are valid, proceed with UTF-8 validation
    i = 0
    while i < len(data):
        byte1 = data[i]
        
        if byte1 < 0x80:
            i += 1
        elif 0xC2 <= byte1 <= 0xDF:
            if i + 1 >= len(data) or not (0x80 <= data[i + 1] <= 0xBF):
                return False
            i += 2
        elif 0xE0 <= byte1 <= 0xEF:
            if i + 2 >= len(data) or not (0x80 <= data[i + 1] <= 0xBF) or not (0x80 <= data[i + 2] <= 0xBF):
                return False
            i += 3
        elif 0xF0 <= byte1 <= 0xF4:
            if i + 3 >= len(data) or not (0x80 <= data[i + 1] <= 0xBF) or not (0x80 <= data[i + 2] <= 0xBF) or not (0x80 <= data[i + 3] <= 0xBF):
                return False
            i += 4
        else:
            return False
        
    return True