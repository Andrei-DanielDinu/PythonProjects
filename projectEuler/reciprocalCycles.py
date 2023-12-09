def recurring_cycle_length(d):
    remainder_position = {}
    remainder = 1
    position = 0

    while remainder not in remainder_position and remainder != 0:
        remainder_position[remainder] = position
        remainder *= 10
        remainder %= d
        position += 1

    return position - remainder_position.get(remainder, 0)

def longest_recurring_cycle(limit):
    max_length = 0
    number = 0

    for d in range(1, limit):
        length = recurring_cycle_length(d)
        if length > max_length:
            max_length = length
            number = d

    return number

result = longest_recurring_cycle(1000)
print("Value of d with the longest recurring cycle:", result)
