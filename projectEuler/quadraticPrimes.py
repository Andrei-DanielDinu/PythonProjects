def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def consecutive_primes():
    max_primes = 0
    product = 0

    for a in range(-999, 1000):
        for b in range(-1000, 1001):
            n = 0
            while is_prime(n * n + a * n + b):
                n += 1
            if n > max_primes:
                max_primes = n
                product = a * b

    return product

result = consecutive_primes()
print(f"The product of coefficients producing the maximum consecutive primes is: {result}")
