from itertools import permutations
import sympy

largest_pandigital_prime = 0

for n in range(7, 0, -1):
    digits = ''.join(str(d) for d in range(1, n + 1))
    pandigital_numbers = list(permutations(digits))
    for pandigital in pandigital_numbers[::-1]:
        num = int(''.join(pandigital))
        if sympy.isprime(num):
            largest_pandigital_prime = num
            break
    if largest_pandigital_prime != 0:
        break

print(f"The largest pandigital prime is: {largest_pandigital_prime}")
