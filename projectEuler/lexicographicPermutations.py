from math import factorial

def millionth_lexicographic_permutation():
    digits = list(range(10))  # Digits 0 to 9
    target_permutation = 1000000  # Millionth permutation

    millionth_permutation = ''
    target_permutation -= 1  # Adjust to zero-based indexing

    for i in range(10, 0, -1):
        index = target_permutation // factorial(i - 1)
        digit = digits.pop(index)
        millionth_permutation += str(digit)
        target_permutation %= factorial(i - 1)

    return millionth_permutation

result = millionth_lexicographic_permutation()
print(f"The millionth lexicographic permutation is: {result}")
