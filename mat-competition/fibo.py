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


FibArray = [1, 2]
 
def calc_fibo(n):
    # than len(FibArray)

    if n <= len(FibArray):
        return FibArray[n - 1]
    else:
        num = n % 50
        length = len(FibArray)
        for i in range(length, num):
            temp_fib = (FibArray[i-1] +FibArray[i-2]) % 10
            FibArray.append(temp_fib)
        return FibArray[num-1]
    
tests = get_number()
for i in range(tests):
    fibo = get_number()
    print(calc_fibo(fibo))

