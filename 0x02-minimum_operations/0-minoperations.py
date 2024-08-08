#!/usr/bin/python3
"""
This module defines a function to calculate the minimum number of operations
required to reach a number `n` starting from 1.
"""


def minOperations(n: int) -> int:
    """
    Calculate the minimum number of operations required to reach `n` starting from 1,
    using only copy and paste operations.

    Args:
        n (int): The target number.

    Returns:
        int: The minimum number of operations.
    """
    if n <= 1:
        return 0

    operations = 0
    factor = 2
    
    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations
