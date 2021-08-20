"""
Your task is to efficiently calculate values ab modulo 10^9+7.

Input:

The first input line contains an integer n: the number of calculations.

After this, there are n lines, each containing two integers a and b.
"""
def calc_expo(a,b, modulu):
    if b == 0:
        return 1
    if b % 2 == 0:
        first = calc_expo(a, b/2, modulu)
        first = (first * first) % modulu 
    if b % 2 == 1:
        first = calc_expo(a,b-1,modulu)
        first = (first * a ) % modulu
    return first

def run_tests():
    tests = int(input())
    mod = pow(10,9) + 7
    for i in range(tests):
        a, b = map(int, input().split())
        print(calc_expo(a,b, mod))