
def is_prime(val):
  div = 2
  while div*div <= val:
    if val % div == 0:
      return False
    div += 1
  return True

fr, to = 55_000_000, 60_000_000
mas = []
for p in range(3, int(to**0.25) + 10):
  if not is_prime(p): continue
  for d in range(0, 30):
    val = 2**d * p**4
    if fr <= val <= to:
      mas += [(val, p**4)]

mas.sort()
for a, b in mas:
  print(a, b)