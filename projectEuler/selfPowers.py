def last_ten_digits_of_series():
    MOD = 10 ** 10  # Modulo value to obtain the last ten digits

    total_sum = 0
    for i in range(1, 1001):
        # Calculate i^i modulo MOD and add it to the total sum
        total_sum += pow(i, i, MOD)
        total_sum %= MOD  # Keep the running sum modulo MOD for efficiency

    return total_sum

