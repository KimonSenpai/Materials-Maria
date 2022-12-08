def f(x, y):
  return 5 + x*15 + 3*15**2 + 2*15**3 + 1*15**4 \
        + 9 + y*17 + 7*17**2 + 6*17**3

for y in range(0, 17):
  for x in range(0, 15):
    val = f(x, y)
    if val % 131 == 0:
      print(val // 131)
      exit()