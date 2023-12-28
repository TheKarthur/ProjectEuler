import sys
import math

def sieve_of_eratosthenes(limit):
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False

    for i in range(2, int(limit**0.5) + 1):
        if primes[i]:
            for j in range(i*i, limit + 1, i):
                primes[j] = False

    return [x for x in range(limit + 1) if primes[x]]

def find_nth_prime(n):
    limit = n * (int(n * (math.log(n) + math.log(math.log(n)))))
    primes = sieve_of_eratosthenes(limit)
    return primes[n - 1]

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(find_nth_prime(n))