def sum_proper_divisors(n):
    divisors_sum = 1  # Start with 1 as a divisor

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors_sum += i
            if i != n // i:  # Avoid counting square root twice
                divisors_sum += n // i

    return divisors_sum

def find_abundant_numbers(limit):
    abundant_numbers = []
    for num in range(12, limit + 1):
        if sum_proper_divisors(num) > num:
            abundant_numbers.append(num)
    return abundant_numbers

def non_sum_of_abundant(limit):
    abundant_list = find_abundant_numbers(limit)
    abundant_sums = set()
    for i in range(len(abundant_list)):
        for j in range(i, len(abundant_list)):
            abundant_sum = abundant_list[i] + abundant_list[j]
            if abundant_sum <= limit:
                abundant_sums.add(abundant_sum)
    non_abundant_sums = set(range(1, limit + 1)) - abundant_sums
    return sum(non_abundant_sums)

limit = 28123
result = non_sum_of_abundant(limit)
print(f"The sum of positive integers not expressible as the sum of two abundant numbers is: {result}")
