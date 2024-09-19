#!/usr/bin/python3
"""Defines the makeChange function to determine the minimum number of coins."""


def makeChange(coins, total):
    """
    Determines the minimum number of coins needed to meet a given total.
    """
    if total <= 0:
        return 0

    d = [{'nm': 0, 'nt': 0}]
    visited = set((0, 0))  # Ensure proper spacing after commas
    while d:
        a = d.pop(0)

        for coin in coins:
            if coin == 0:
                continue
            new_nm = a['nm'] + 1
            new_nt = coin + a['nt']

            if new_nt < total and (new_nm, new_nt) not in visited:
                visited.add((new_nm, new_nt))
                d.append({'nm': new_nm, 'nt': new_nt})

            if new_nt == total:
                return new_nm

    return -1
