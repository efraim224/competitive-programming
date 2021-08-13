import math

def count_pos(n):
    possibilities = []
    # base case
    possibilities.insert(0, 1)
    for index in range(1,n):
        count = 0
        if index < 6:
            for i in range(0,index):
                count += possibilities[i]
            count += 1
        else:
            for i in range(index - 6,index):
                count += possibilities[i]
        possibilities.insert(index,count)
    if n > 990:
        print([possibilities[999]])
        print([possibilities[998]])
        print([possibilities[997]])
        print([possibilities[996]])
        print([possibilities[995]])
        print([possibilities[994]])
        
    print(possibilities[n -1])

read = int(input())
count_pos(read)