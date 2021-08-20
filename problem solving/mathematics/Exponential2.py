import Exponential

"""
Your task is to efficiently calculate values a^(b^c) modulo 10^9+7.

Input

The first input line has an integer n: the number of calculations.

Afther this, there are n lines, each containing three integers a, b and c.

Output

Print each value abc modulo 10^9+7.
"""
mod = pow(10,9) + 7
tests = int(input())
for i in range(tests):
    list = [int(x) for x in input().split()]
    power = Exponential.calc_expo(list[1],list[2],mod)
    ans = Exponential.calc_expo(list[0],power, mod)
    print(ans)
