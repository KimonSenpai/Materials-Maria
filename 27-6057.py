
for file in ("27_A (2).txt", "27_B (2).txt"):
  f = open(file)

  N = int(f.readline())
  S, dif = 0, 10000
  for line in f:
    a, b, c = sorted(map(int, line.split()), reverse=False)

    S += c
    if (c - b) % 91 != 0:
      dif = min(dif, c - b)
    if (c - a) % 91 != 0:
      dif = min(dif, c - a)

  if S % 91 == 0:
    S -= dif
  print(S, end=" ")
