#!/usr/bin/python3
"""Find perimeter of the island
"""


def island_perimeter(grid):
    """Method returns the perimeter of the island described in grid.
    """
    a = 0
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            if grid[i][j] == 1:
                if i + 1 >= len(grid) or grid[i + 1][j] == 0:
                    a += 1
                if j + 1 >= len(grid[i]) or grid[i][j + 1] == 0:
                    a += 1
                if i - 1 < 0 or grid[i - 1][j] == 0:
                    a += 1
                if j - 1 < 0 or grid[i][j - 1] == 0:
                    a += 1
    return a
