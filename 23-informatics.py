from functools import lru_cache

@lru_cache(None)
def f(fr, to):
  if fr == to:
    return 1
  if fr > to:
    return 0

  res = f(fr, to - 1) + f(fr, to - 2)
  if to % 2 == 0:
    res += f(fr, to // 2)
  
  return res

print(f(3, 10)*f(10, 12))
