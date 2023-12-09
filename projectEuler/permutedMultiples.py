def has_same_digits(n, m):
    return sorted(str(n)) == sorted(str(m))

found = False
x = 1

while not found:
    if all(has_same_digits(x, x * i) for i in range(2, 7)):
        found = True
    else:
        x += 1

print("The smallest positive integer is:", x)
