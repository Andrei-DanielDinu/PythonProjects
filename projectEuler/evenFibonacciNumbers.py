# Initialize variables
a, b = 1, 2
sum_even = 0

# Loop to generate Fibonacci sequence and sum even values
while a <= 4000000:
    if a % 2 == 0:
        sum_even += a
    a, b = b, a + b

print("The sum of even-valued terms:", sum_even)
