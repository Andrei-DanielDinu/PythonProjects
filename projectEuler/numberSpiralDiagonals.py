def sum_of_diagonals_in_spiral(size):
    total = 1  # Start with the center number (1x1 spiral)

    # Calculate the sum for each layer of the spiral
    for n in range(3, size + 1, 2):
        total += 4 * (n ** 2) - 6 * (n - 1)

    return total

# For a 1001x1001 spiral
size = 1001
result = sum_of_diagonals_in_spiral(size)
print(f"The sum of the numbers on the diagonals in a {size}x{size} spiral is: {result}")
