#!/usr/bin/python3
"""
validUTF8 Module
"""


def validUTF8(data: list) -> bool:
    """
        Function validUTF8 to validate the utf-8 encoding
    """
    num_bytes = 0

    # Masks to check the most significant bits
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for byte in data:
        mask = 1 << 7
        if num_bytes == 0:
            # Count the number of leading 1's in the current byte
            while byte & mask:
                num_bytes += 1
                mask >>= 1

            # If num_bytes is 0, then it's a 1-byte character
            if num_bytes == 0:
                continue

            # UTF-8 characters can only be 1 to 4 bytes long
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            # If this byte does not start with '10', then it's not valid
            if not (byte & mask1 and not (byte & mask2)):
                return False

        num_bytes -= 1

    # If num_bytes is not 0, then we have an incomplete character at the end
    return num_bytes == 0
