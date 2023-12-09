def is_palindromic(string):
    return string == string[::-1]

def sum_dual_palindromes(limit):
    total_sum = 0

    for num in range(1, limit):
        base_10 = str(num)
        base_2 = bin(num)[2:]  # Binary representation without '0b' prefix

        if is_palindromic(base_10) and is_palindromic(base_2):
            total_sum += num

    return total_sum

limit = 1000000
result = sum_dual_palindromes(limit)
print(f"The sum of numbers palindromic in both base 10 and base 2 is: {result}")
