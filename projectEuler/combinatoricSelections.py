from math import comb

count = 0
for n in range(1, 101):
    for r in range(1, n):
        if comb(n, r) > 10**6:
            count += 1

print("Count of binomial coefficients exceeding one million:", count)
