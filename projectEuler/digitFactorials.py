from math import factorial

def sum_factorial_digits():
    total_sum = 0

    # Iterate through numbers to check if they satisfy the condition
    for num in range(10, 100000):  # Assuming upper limit
        if num == sum(factorial(int(digit)) for digit in str(num)):
            total_sum += num

    return total_sum

result = sum_factorial_digits()
print(f"The sum of all numbers equal to the sum of the factorial of their digits is: {result}")
