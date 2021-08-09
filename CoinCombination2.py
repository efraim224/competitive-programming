def coin_combo2():
    coins_sum = input().split()
    sum =  int(coins_sum[1])
    value_str = input().split()
    coin_values = [int(x) for x in value_str]
    combination = [0]
    for amount in range(1, sum+1):
        total = 0
        for coin in coin_values:
            if amount - coin > 0:
                total += combination[amount-coin]
            if amount -coin == 0:
                total += 1
        combination.insert(amount, total)
    print(combination[sum])

coin_combo2()