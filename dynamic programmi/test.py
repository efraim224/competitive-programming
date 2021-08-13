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
        
def Sort_Tuple(tup): 

    tup.sort(key = lambda x: x[1]) 
    return tup


numOfMembers = get_number()
list = []
for i in range (0,numOfMembers):
    name = get_word()
    height = get_number()
    list.append((name,height))
list = Sort_Tuple(list)
list = list[::-1]
for member in list:
   print(member)

print("yes")
