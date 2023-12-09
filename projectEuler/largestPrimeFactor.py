def largest_prime_factor(n):
    factor = 2
    while factor * factor <= n:
        if n % factor == 0:
            n //= factor
        else:
            factor += 1
    return n

number = 600851475143
result = largest_prime_factor(number)
print("The largest prime factor of", number, "is:", result)
