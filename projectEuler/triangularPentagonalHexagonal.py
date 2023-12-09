def generate_triangle(n):
    return n * (n + 1) // 2

def generate_pentagonal(n):
    return n * (3 * n - 1) // 2

def generate_hexagonal(n):
    return n * (2 * n - 1)

def find_special_number():
    # Start checking from the provided indices
    index_t = 286
    index_p = 165
    index_h = 143

    while True:
        triangle = generate_triangle(index_t)
        pentagonal = generate_pentagonal(index_p)
        hexagonal = generate_hexagonal(index_h)

        min_value = min(triangle, pentagonal, hexagonal)
        if triangle == pentagonal == hexagonal == min_value:
            return triangle

        if min_value == triangle:
            index_t += 1
        if min_value == pentagonal:
            index_p += 1
        if min_value == hexagonal:
            index_h += 1

result = find_special_number()
print(f"The next triangle number that is also pentagonal and hexagonal is: {result}")
