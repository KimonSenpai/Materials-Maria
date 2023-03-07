
def to_seven(val):
  res = ""
  while val > 0:
    res = f"{val%7}" + res
    val //= 7
  return res


cnt = 0
for val in range(7**5, 7**6):
  s = to_seven(val)
  good = True

  if s.count('6') != 1:
    continue

  for i in range(5):
    if int(s[i]) % 2 == int(s[i+1]) % 2:
      good = False
      break
  
  if good: cnt += 1

print(cnt)
