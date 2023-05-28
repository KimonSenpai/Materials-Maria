from functools import lru_cache

def go(a, b):
    return [f(a*2, b), f(a, b*2), f(a + 2, b), f(a, b + 2)]

@lru_cache(None)
def f(a, b):
    if a + b >= 63:
        if a + b <= 74:
            return -1
        else:
            return +1
    
    mas = go(a, b)

    if all(v > 0 for v in mas):
        return -max(mas) - 1
    else:
        return -max(v for v in mas if v < 0) + 1
    
for s in range(1, 48):
    if +2 in go(15, s) and any(v < 0 for v in go(15, s)):
        print(s)

print('====================')

for s in range(1, 48):
    if f(15, s) == +4:
        print(s)

for s in range(1, 48):
    if f(15, s) == +4 or f(15, s) == +5:
        print(s)

print('=====================')

for s in range(1, 48):
    if f(15, s) == -5 or f(15, s) == -6:
        print(s)