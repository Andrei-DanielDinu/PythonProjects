import math

result = 1
for i in range(1, 21):
    result = result * i // math.gcd(result, i)

print("The smallest number divisible by all numbers from 1 to 20 is:", result)
