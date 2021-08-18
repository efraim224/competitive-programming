def calc_expo(a,b, modulu):
    if b == 0:
        return 1
    u = calc_expo(a,b/2, modulu)
    u = (u*u) % modulu
    if b % 2 == 1:
        u = (u*a) % modulu
    return u


tests = int(input())
mod = pow(10,9) + 7
for i in range(tests):
    a, b = map(int, input().split())
    print(calc_expo(a,b, mod))