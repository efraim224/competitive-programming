# a simple parser for python. use get_number() and get_word() to read
def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield(number)   

input_parser = parser()

def get_word():
    global input_parser
    return next(input_parser)

def get_number():
    data = get_word()
    try:
        return int(data)
    except ValueError:
        return float(data)


def calculate_this(list, place, money):
    res = -1
    if place == len(list) -1:
        for i in range(0,len(list[place])):
            if money >= list[place][i]:
                res = max(res, list[place][i])
        return res
    else:
        for i in range(0,len(list[place])):
            if money >= list[place][i]:
                after = calculate_this(list, place + 1, money - list[place][i])
                if after > -1:
                    res = after + list[place][i]
        return res
            
        

# numpy and scipy are available for use
# import numpy
# import scipy
tests = get_number()
for i in range(0,tests):
    money = get_number()
    components = get_number()
    cost_compontnts = []
    line = input()
    for comp in range(0,components):
        line = [int(x) for x in input().split(' ') if int(x) <= money]
        cost_compontnts.insert(comp, line)
    ans = 0
    for i in range(0, len(cost_compontnts[0])):
        ans = max(ans, calculate_this(cost_compontnts,0, money))
    print(ans)
            

    