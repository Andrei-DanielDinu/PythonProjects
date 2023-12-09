from math import isqrt

def is_s_number(n):
    sqrt_n = isqrt(n)
    str_n = str(n)
    for i in range(1, len(str_n)):
        parts = [int(str_n[:i])]
        for j in range(i, len(str_n)):
            parts.append(int(str_n[i:j+1]))
        if sum(parts) == sqrt_n:
            return True
    return False

def T(n):
    total = 0
    for i in range(1, n + 1):
        if is_s_number(i):
            total += i
    return total

result = T(10 ** 12)
print("T(10^12) =", result)
