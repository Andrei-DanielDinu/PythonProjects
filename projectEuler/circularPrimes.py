def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_rotations(n):
    str_n = str(n)
    rotations = [int(str_n[i:] + str_n[:i]) for i in range(len(str_n))]
    return rotations

def count_circular_primes(limit):
    circular_prime_count = 0

    for num in range(2, limit):
        if all(is_prime(rotation) for rotation in generate_rotations(num)):
            circular_prime_count += 1

    return circular_prime_count

limit = 1000000
result = count_circular_primes(limit)
print(f"The number of circular primes below one million is: {result}")
