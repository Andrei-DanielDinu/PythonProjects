def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_truncatable_prime(n):
    str_n = str(n)
    for i in range(len(str_n)):
        if not is_prime(int(str_n[i:])) or not is_prime(int(str_n[:i + 1])):
            return False
    return True

count = 0
num = 10  # Starting from 10 to skip single digit primes
total = 0

while count < 11:
    if is_truncatable_prime(num):
        total += num
        count += 1
    num += 1

print("The sum of the truncatable primes is:", total)
