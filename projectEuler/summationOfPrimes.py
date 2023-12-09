def sieve_of_eratosthenes(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    p = 2
    while p * p <= limit:
        if sieve[p]:
            for i in range(p * p, limit + 1, p):
                sieve[i] = False
        p += 1
    return [i for i in range(2, limit + 1) if sieve[i]]

# Define the limit as two million
limit = 2000000

# Get all primes below two million using the sieve
primes = sieve_of_eratosthenes(limit)

# Sum all the primes
sum_of_primes = sum(primes)

print("The sum of all primes below two million is:", sum_of_primes)
