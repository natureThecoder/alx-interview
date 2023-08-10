#!/usr/bin/python3
"""
Minimum Operations
"""


def minOperations(n):
    k = 0
    z = 2

    while n > 1:
        while n % z == 0:
            k += z
            n /= z
        z += 1
    return k

