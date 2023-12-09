from itertools import permutations

pandigital_products = set()

for perm in permutations("123456789"):
    perm = "".join(perm)
    for i in range(1, len(perm)):
        for j in range(i + 1, len(perm)):
            multiplicand = int(perm[:i])
            multiplier = int(perm[i:j])
            product = int(perm[j:])
            if multiplicand * multiplier == product:
                pandigital_products.add(product)

sum_of_pandigital_products = sum(pandigital_products)
print(f"The sum of pandigital products is: {sum_of_pandigital_products}")
