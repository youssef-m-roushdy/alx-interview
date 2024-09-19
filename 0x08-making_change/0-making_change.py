#!/usr/bin/python3
"""Defines the makeChange function to determine the minimum number of coins."""
from collections import deque


def makeChange(coins, total):
    """
    Determines the minimum number of coins needed to meet a given total.
    """
    if total <= 0:
        return 0

    # Queue to store states of (number of coins used, current total)
    d = deque([(0, 0)])  # (number of coins, current total)

    # Set to track visited total amounts
    visited = set([0])  # Only track total, since BFS ensures minimum coins

    while d:
        num_coins, curr_total = d.popleft()

        for coin in coins:
            new_total = curr_total + coin

            if new_total == total:
                return num_coins + 1
            if new_total < total and new_total not in visited:
                visited.add(new_total)
                d.append((num_coins + 1, new_total))

    return -1  # If no combination can form the total
