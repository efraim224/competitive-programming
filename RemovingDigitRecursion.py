def remove_digit(num):
    if num == 0:
        return 0
    digit_list = [int(x) for x in str(num)]
    digit = max(digit_list)
    res = 1 + remove_digit(int(num) - digit)
    return res

num = input()
print(remove_digit(num))