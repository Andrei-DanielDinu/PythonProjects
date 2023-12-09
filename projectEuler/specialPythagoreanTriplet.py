def find_pythagorean_triplet(target_sum):
    for a in range(1, target_sum // 3):
        for b in range(a + 1, target_sum // 2):
            c = target_sum - a - b
            if a * a + b * b == c * c:
                return a * b * c

target_sum = 1000
result = find_pythagorean_triplet(target_sum)
print("The product of the Pythagorean triplet is:", result)
