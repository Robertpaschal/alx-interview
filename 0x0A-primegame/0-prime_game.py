#!/usr/bin/python3
""" Module containing the game-winner function"""


# 0-prime_game.py

def isWinner(x, nums):
    """Function defining constraints for the game-winner"""
    def count_primes_up_to(n):
        """ Returns the number of primes <= n using the Sieve of Eratosthenes. """
        if n < 2:
            return 0
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False
        for start in range(2, int(n**0.5) + 1):
            if is_prime[start]:
                for multiple in range(start*start, n + 1, start):
                    is_prime[multiple] = False
        return sum(is_prime)
    
    maria_wins = 0
    ben_wins = 0
    
    for n in nums:
        prime_count = count_primes_up_to(n)
        if prime_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1
    
    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    else:
        return None
