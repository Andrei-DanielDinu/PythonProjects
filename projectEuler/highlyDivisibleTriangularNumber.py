import math

def count_divisors(num):
    count = 0
    sqrt = int(math.sqrt(num))
    for i in range(1, sqrt + 1):
        if num % i == 0:
            count += 2 if i < sqrt else 1
    return count

def find_triangle_number(divisors):
    n = 1
    triangle = 0
    while True:
        triangle += n
        if count_divisors(triangle) > divisors:
            return triangle
        n += 1

required_divisors = 500
result = find_triangle_number(required_divisors)
print(f"The first triangle number with over {required_divisors} divisors is: {result}")
