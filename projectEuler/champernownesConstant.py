def find_digit_product():
    fractional_part = ''.join(str(i) for i in range(1, 1000000))  # Create concatenated string
    indices = [1, 10, 100, 1000, 10000, 100000, 1000000]
    product = 1

    for idx in indices:
        product *= int(fractional_part[idx - 1])  # Subtract 1 due to 0-based indexing

    return product

result = find_digit_product()
print(f"The product of specified digits is: {result}")
