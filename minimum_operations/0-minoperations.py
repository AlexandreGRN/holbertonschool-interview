#!/usr/bin/python3
"""
Minimum Operations
"""


def minOperations(number):

    if number <= 1:
        return 0

    total_operations = 0
    divisor = 2

    while divisor <= number:
        while number % divisor == 0:
            total_operations += divisor
            number //= divisor
        divisor += 1

    return total_operations
