def sum_of_digit_powers(number, power):
    return sum(int(digit) ** power for digit in str(number))

def sum_of_numbers_with_digit_powers(power):
    result_sum = 0

    # Iterate through numbers to find the ones satisfying the condition
    for num in range(10, 1000000):  # Assuming upper limit
        if num == sum_of_digit_powers(num, power):
            result_sum += num

    return result_sum

power = 5  # Fifth powers of digits
result = sum_of_numbers_with_digit_powers(power)
print(f"The sum of all numbers that can be written as the sum of {power}th powers of their digits is: {result}")
