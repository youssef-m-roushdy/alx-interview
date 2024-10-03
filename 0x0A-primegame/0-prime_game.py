#!/usr/bin/python3
def is_prime(n):
    """
    Check if a number is prime.
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def isWinner(x, nums):
    """
    Determines the winner of the game after x rounds.
    x: number of rounds
    nums: list of numbers for each round
    Returns: Name of the player with the highest wins, or None if it's a tie.
    """
    primes = set()
    players = {"Maria": 0, "Ben": 0}

    for i in range(x):
        prime_count = 0
        for j in range(2, nums[i] + 1):
            if j not in primes and is_prime(j):
                primes.add(j)
                prime_count += 1
        if prime_count % 2 == 1:
            players["Ben"] += 1
        else:
            players["Maria"] += 1

    if players["Maria"] > players["Ben"]:
        return "Maria"
    elif players["Ben"] > players["Maria"]:
        return "Ben"
    else:
        return None
