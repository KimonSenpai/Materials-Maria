resoult = 0
for val in range(8**5, 8**6):
  if val % 5 != 0:
    continue
  last = val%8
  val //= 8
  digs = [last]
  
  good = True
  while val > 0:
    if val%2 == last%2:
      good = False
      break
    last = val%8
    val //= 8
    digs += [last]

  if not good: continue
  if len(digs) == len(set(digs)): resoult += 1


print(resoult)
