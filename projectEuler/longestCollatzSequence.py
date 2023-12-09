def collatz_chain_length(n):
    length = 1
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        length += 1
    return length

def longest_collatz_chain(limit):
    max_length = 0
    starting_number = 0
    for i in range(1, limit):
        length = collatz_chain_length(i)
        if length > max_length:
            max_length = length
            starting_number = i
    return starting_number, max_length

limit = 1000000
result = longest_collatz_chain(limit)
print(f"The starting number under {limit} producing the longest chain is: {result[0]}")
print(f"The chain length is: {result[1]}")
