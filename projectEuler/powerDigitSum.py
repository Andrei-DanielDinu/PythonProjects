# Calculate 2^1000
power = str(2 ** 1000)

# Find the sum of its digits
digit_sum = sum(int(digit) for digit in power)

print("The sum of the digits of 2^1000 is:", digit_sum)
