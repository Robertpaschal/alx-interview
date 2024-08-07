#!/usr/bin/python3
""" Module containing the game-winner function"""


def isWinner(x, nums):
    """Function defining contraints for the game-winner"""
    def sieve(n):
        """Return a list of primes up to n using Sieve of Erastothenes"""
        is_prime = [True] * (n + 1)
        p = 2
        while p * p <= n:
            if is_prime[p]:
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1
        return [p for p in range(2, n + 1) if is_prime[p]]

    def play_game(n):
        """ Simulate the game for given n
        and return the winner: 'Maria' or 'Ben """
        primes = sieve(n)
        if not primes:
            return 'Ben'
        # Boolean list to keep track of available numbers
        available = [True] * (n + 1)
        current_player = 0   # 0 for Maria, 1 for Ben

        while primes:
            prime = primes[0]
            # Remove the prime and its multiples
            for multiple in range(prime, n + 1, prime):
                available[multiple] = False

            # remove used prime from the list
            primes.pop(0)

            # check if thers area any primes left for the next player
            next_available_primes = [p for p in range(
                2, n + 1) if available[p] and p in primes]
            if not next_available_primes:
                return 'Maria' if current_player == 1 else 'Ben'

            # Switch player
            current_player = 1 - current_player
        return 'Maria' if current_player == 1 else 'Ben'
    if x <= 0 or not nums:
        return None

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = play_game(n)
        if winner == 'Maria':
            maria_wins += 1
        elif winner == 'Ben':
            ben_wins += 1

    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    else:
        return None
