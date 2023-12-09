def nth_prime(n):
    primes = []
    num = 2
    while len(primes) < n:
        is_prime = True
        for prime in primes:
            if num % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
        num += 1
    return primes[-1]

nth = 10001
result = nth_prime(nth)
print("The 10,001st prime number is:", result)
