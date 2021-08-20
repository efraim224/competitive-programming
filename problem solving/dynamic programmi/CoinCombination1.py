import math

def coin_combination():
    coins_sum = input().split()
    sum =  int(coins_sum[1])
    value_str = input().split()
    coin_values = [int(x) for x in value_str]
    combination = [[0]]
    for amount in range(1, sum +1):
        coin_combo = []
        for coin in coin_values:
            if amount - coin >= 0:
                for combo in combination[amount - coin]:
                    coin_combo.append(combo+1)
        combination.insert(amount, coin_combo)
    print(len(combination[sum]))


coin_combination()