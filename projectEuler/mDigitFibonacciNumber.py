def fibonacci_digits(n):
    a, b = 1, 1
    index = 2  # Start from F_2 (index 2)

    while True:
        index += 1
        a, b = b, a + b  # Calculate the next Fibonacci number
        if len(str(b)) >= n:
            return index  # Return the index if the number has n digits


result = fibonacci_digits(1000)
print("Index of the first term in the Fibonacci sequence with 1000 digits:", result)
