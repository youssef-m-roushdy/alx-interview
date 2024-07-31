#!/usr/bin/python3
"""
Module to determine if all boxes can be unlocked
"""

def canUnlockAll(boxes):
    """
    Determines if all the boxes can be unlocked.

    Args:
        boxes (list of lists): A list where each element is a list of keys.

    Returns:
        bool: True if all boxes can be unlocked, False otherwise.
    """
    # List to keep track of which boxes have been opened
    opened = [False] * len(boxes)
    opened[0] = True  # Box 0 is always open

    # Stack to keep track of the boxes to check next
    stack = [0]

    # While there are boxes to check
    while stack:
        current_box = stack.pop()

        for key in boxes[current_box]:
            if key < len(boxes) and not opened[key]:
                opened[key] = True
                stack.append(key)

    # Check if all boxes are opened
    return all(opened)
