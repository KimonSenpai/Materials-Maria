from functools import lru_cache

def move(a, b):
    aa = [a // 10, a % 10]
    bb = [b // 10, b % 10]

    res = []

    for da in aa:
        for db in bb:
            na = da*10 + db
            nb = db*10 + da

            if na < a:
                res += [(na, b)]
            if nb < b:
                res += [(a, nb)]
    return res


def go(a, b):
    return [f(*e) for e in move(a, b)]

def f(a, b):
    if len(move(a, b)) == 0:
        return -0
    
    mas = go(a, b)

    if all(v > 0 for v in mas):
        return -max(mas) - 1
    else:
        return -max(v for v in mas if v <= 0) + 1
if False:
  for a in range(10, 100):
      for b in range(10, 100):
          if f(a, b) == -2:
              print(a, b)
if False:
  print(f(23, 31))
  for a, b in zip(move(23,31), go(23, 31)):
      print(a, b)

print(f(52, 31))
for a, b in zip(move(52, 31), go(52, 31)):
    print(a, b)