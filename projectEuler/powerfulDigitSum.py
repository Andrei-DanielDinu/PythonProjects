def digit_sum(n):
    return sum(int(digit) for digit in str(n))

max_digital_sum = 0

for a in range(1, 100):
    for b in range(1, 100):
        power = a ** b
        digit_sum_power = digit_sum(power)
        if digit_sum_power > max_digital_sum:
            max_digital_sum = digit_sum_power

print(f"The maximum digital sum is: {max_digital_sum}")
