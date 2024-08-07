#!/usr/bin/python3
""" Module containing the game-winner function"""


def isWinner(x, nums):
    """Function defining constraints for the game-winner"""
    def sieve(n):
        """Return a list of primes up to n using Sieve of Eratosthenes"""
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
        and return the winner: 'Maria' or 'Ben' """
        primes = sieve(n)
        if not primes:
            return 'Ben'
        # Boolean list to keep track of available numbers
        available = [True] * (n + 1)
        current_player = 0  # 0 for Maria, 1 for Ben

        while True:
            move_made = False
            for prime in primes:
                if available[prime]:
                    for multiple in range(prime, n + 1, prime):
                        available[multiple] = False
                    move_made = True
                    break

            if not move_made:
                return 'Maria' if current_player == 1 else 'Ben'

            current_player = 1 - current_player

    if x <= 0 or not nums:
        return None

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = play_game(n)
        print(f"Game with n={n} won by {winner}")  # Debug print
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
