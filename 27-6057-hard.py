for file in ["27_A (2).txt", "27_B (2).txt"]:
  f = open(file)

  N = int(f.readline())
  mas = [-1]*91
  mas[0] = 0

  for line in f:
    a, b, c = map(int, line.split())
    n_mas = [-1]*91
    for val in (a, b, c):
      for i in range(0, 91):
        if mas[i] != -1:
          n_mas[(i + val)%91] = max(n_mas[(i + val)%91], mas[i] + val)
    mas = n_mas
  print(max(mas[1:]), end=' ')