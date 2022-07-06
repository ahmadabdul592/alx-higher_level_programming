#!/usr/bin/python3
"""
Returns a list of lists of integers
representing the Pascal’s triangle of n.
"""


def pascal_triangle(n):
    """Returns the pascal triangle of n.
    Args:
        - n: size of the triangle (rows)
    Returns: a list of list of integers
    """

    if n <= 0:
        return []

    la = [[0 for x in range(i + 1)] for i in range(n)]
    la[0] = [1]

    for i in range(1, n):
        la[i][0] = 1
        for j in range(1, i + 1):
            if j < len(la[i - 1]):
                la[i][j] = la[i - 1][j - 1] + la[i - 1][j]
            else:
                la[i][j] = la[i - 1][0]
    return la
