from functools import lru_cache

@lru_cache(None)
def f(fr, to):
  if fr == to:
    return 1
  if fr > to or to == 15:
    return 0

  return f(fr, to - 1) + f(fr, to - 2)

print(f(3, 9)*f(9, 20))

@lru_cache(None)
def f2(fr, to):
  if fr == to:
    return 1
  if fr > to:
    return 0

  return f2(fr, to - 1) + f2(fr, to - 2)

print(f2(3, 9)*f2(9, 20) - f2(3, 9)*f2(9, 15)*f2(15, 20))