def increasing_sub(list, N):
    sub = [-1] * (N )
    sub[0] = 1
    for i in range(1,N):
        current = 0
        for j in range(i,-1,-1):
            if list[j] < list[i]:
                current = max(current, sub[j] + 1)
            else:
                current = max(current,1)
        sub[i] = current
    print(max(sub))


length = int(input())
list = [int(x) for x in input().split()]
increasing_sub(list,length)