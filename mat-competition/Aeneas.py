import math

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


def calculate_line(angle, length):
    if angle == 180:
        return length * 2
    return math.sqrt((2 * pow(length,2) * (1 - math.cos(math.radians(angle)))))


def calc_angle(first, second):
    res = abs(first - second)
    if res > 180:
        res += -180
    return res


length = get_number()
letters = []
angles = []
for i in range(26):
    letter = get_word()
    angle = get_number()
    letters.insert(i,letter)
    angles.insert(i, angle)

word = input().upper()
first = ""
count = length
for char in word:
    if char.isalpha() and first == "":
        first = char
    elif char.isalpha():
        second = char
        first_index= int(letters.index(first))
        second_index = int(letters.index(second))
        current_angle = calc_angle(angles[first_index], angles[second_index])
        if first != second:
            res = (calculate_line(current_angle, length))
            print(res)
            count = count + res 
        first = second
    
print(count)

