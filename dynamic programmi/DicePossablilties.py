import math

def count_pos(n):
    sum = []
    # base case
    sum.insert(0, 1)
    for index in range(1,n):
        count = 0
        if index < 6:
            for i in range(0,index):
                count += sum[i]
            count += 1
        else:
            for i in range(index - 6,index):
                count += sum[i]
        count = count % (math.pow(10,9) + 7)
        sum.insert(index,count)
    ans = sum[n -1]
    print(int(ans))

read = int(input())
count_pos(read)