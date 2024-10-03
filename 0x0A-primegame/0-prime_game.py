#!/usr/bin/python3
def is_prime_sieve(n):
    """Generates a list of booleans indicating if numbers up to n are prime."""
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return sieve


def count_primes(n, prime_sieve):
    """Returns the number of primes up to and including n."""
    return sum(1 for i in range(2, n + 1) if prime_sieve[i])


def isWinner(x, nums):
    """
    Determines the winner of the prime game after x rounds.
    x: number of rounds
    nums: list of numbers representing the upper limit for each round
    Returns: Name of the player with the most wins, or None if it's a tie.
    """
    if not nums or x < 1:
        return None

    max_n = max(nums)
    prime_sieve = is_prime_sieve(max_n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        prime_count = count_primes(n, prime_sieve)

        if prime_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
