import math

def min_coins():
    coins_sum = input().split()
    sum =  int(coins_sum[1])
    value_str = input().split()
    coin_values = [int(x) for x in value_str]
    num_coins = [0]
    for amount in range(1, sum + 1):
        res = math.inf
        for coin in coin_values:
            if amount - coin >= 0:
                res = min(res, num_coins[amount - coin] + 1)
        
        num_coins.insert(amount, res)
    print(num_coins[sum])

min_coins()