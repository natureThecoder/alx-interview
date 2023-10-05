#!/usr/bin/python3
""" Prime Game """


def findMultiples(x, lists):
    """ Find multiples
    """
    for i in lists:
        if i % x == 0:
            lists.remove(i)
    return lists


def isPrime(i):
    """ check for
    primes
    """
    if i == 1:
        return False
    for j in range(2, i):
        if i % j == 0:
            return False
    return True


def picks(lists):
    """ takes a list and
    returns their picks
    """
    counter = 0
    for i in range(1, len(lists) + 1):
        if isPrime(i):
            counter += 1
            lists.remove(i)
            lists = findMultiples(i, lists)
        else:
            pass
    return counter


def isWinner(x, nums):
    """
    Prime game played by Maria and Ben.
    Given a set of consecutive integers
    starting from 1 up to and including n,
    they take turns choosing a prime number
    from the set and removing that number and
    its multiples from the set. The player that
    cannot make a move loses the game.
    """
    players = {'Maria': 0, 'Ben': 0}
    val = []
    for i in range(x):
        val = [j for j in range(1, nums[i] + 1)]
        pick = picks(val)

        if pick % 2 == 0:
            players['Ben'] += 1
        elif pick % 2 != 0:
            players['Maria'] += 1

    if players['Maria'] > players['Ben']:
        return 'Maria'
    elif players['Maria'] < players['Ben']:
        return 'Ben'
    else:
        return None
