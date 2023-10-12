#!/usr/bin/python3
"""Determines minimum operations"""

def minOperations(n):
  """Determines minimum operations"""
    if n < 2:
        return n  # If n is less than 2, no Copy All is needed.

    operations = 0  # Initialize the count of operations.
    clipboard = 0  # Initialize the clipboard.

    while n > 1:
        if n % 2 == 0:
            clipboard = n // 2
        else:
            clipboard = n

        n -= clipboard
        operations += 1

    return operations

if __name__ == "__main__":
    n = 4
    print("Min number of operations to reach {} characters: {}".format(n, minOperations(n)))

    n = 12
    print("Min number of operations to reach {} characters: {}".format(n, minOperations(n)))
