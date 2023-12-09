# Initialize the sum
sum_multiples = 0

# Loop through numbers below 1000
for num in range(1, 1000):
    if num % 3 == 0 or num % 5 == 0:
        sum_multiples += num

print("The sum of multiples of 3 or 5 below 1000 is:", sum_multiples)
