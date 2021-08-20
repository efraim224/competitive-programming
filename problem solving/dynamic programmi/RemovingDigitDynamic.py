def remove_digit(num):
    ans = [0]
    for index in range(1,num+1):
        digits = [int(x) for x in str(index)]
        ans.insert(index, min([digits[x] for x in digits]))
    print(ans[num])

read = int(input())
remove_digit(read)