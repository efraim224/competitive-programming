def count_money(length, list):
    for i in range(0, length):
        count = 0
        for j in range(i,-1,-1):
            count += list[j]
            print(count)
            

count_money(4, [4,2,5,2])