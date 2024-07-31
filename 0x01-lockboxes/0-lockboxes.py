#!/usr/bin/python3

def canUnlockAll(boxes):
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
