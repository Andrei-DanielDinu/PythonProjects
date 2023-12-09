def coin_combinations(target, coins):
    ways = [0] * (target + 1)
    ways[0] = 1  # Base case: One way to make 0p

    for coin in coins:
        for amount in range(coin, target + 1):
            ways[amount] += ways[amount - coin]

    return ways[target]

coins = [1, 2, 5, 10, 20, 50, 100, 200]  # Coin values in pence
target_amount = 200  # Target amount in pence (£2)
ways_to_make_target = coin_combinations(target_amount, coins)

print("Number of ways to make £2 using coins:", ways_to_make_target)
