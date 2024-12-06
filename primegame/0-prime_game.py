#!/usr/bin/python3
""" Prime Game """


def isprime(n):
    """ if n is prime"""
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def isWinner(x, nums):
    """ where x is the number of rounds and nums is an array of n
        Return: name of the player that won the most rounds
        Iriaf the winner cannot be determined, return None
        You can assume n and x will not be larger than 10000
    """
    nums.sort()
    winner = False
    Maria = 0
    Ben = 0
    for game in range(x):
        nums2 = list(range(1, nums[game] + 1))
        turn = 0
        while True:
            change = False
            for i, n in enumerate(nums2):
                if n > 1 and isprime(n):
                    for i in range(len(nums2)):
                        if nums2[i] % n == 0:
                            nums2[i] = 0
                    change = True
                    turn += 1
                    break
            if change is False:
                break
        if turn % 2 != 0:
            Maria += 1
        else:
            Ben += 1
    if Maria == Ben:
        return None
    if Maria > Ben:
        return "Maria"
    return "Ben"
