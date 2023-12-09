# Function to calculate the factorial of a number
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Calculate factorial of 100
factorial_100 = factorial(100)

# Convert the factorial result to a string to sum its digits
factorial_str = str(factorial_100)

# Sum the digits of the factorial result
digit_sum = sum(int(digit) for digit in factorial_str)

print("Sum of digits in 100!:", digit_sum)
