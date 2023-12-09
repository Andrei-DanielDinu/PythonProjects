def sum_of_divisors(n):
    divisors_sum = 1  # 1 is always a divisor
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors_sum += i
            if i != n // i:
                divisors_sum += n // i
    return divisors_sum

def sum_amicable_numbers(limit):
    amicable_sum = 0
    for a in range(2, limit):
        b = sum_of_divisors(a)
        if a != b and sum_of_divisors(b) == a:
            amicable_sum += a
    return amicable_sum

limit = 10000
result = sum_amicable_numbers(limit)
print(f"The sum of all amicable numbers under {limit} is: {result}")
