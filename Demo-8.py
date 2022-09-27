

def f(n=5, last=0, is_six=False):
  if n == 0:
    if is_six:
      return 1
    else:
      return 0
  k = 0
  for dig in range(8):
    if n == 5 and dig == 0: continue
    if last == 6 and dig%2 == 1: continue
    if dig == 6 and last%2 == 1: continue
    if dig == 6 and is_six: continue

    k += f(n-1, dig, is_six or dig==6)
  return k

print(f())