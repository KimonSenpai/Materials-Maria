
def fishka(n):
  if n == 1:
    print(1, end=' ')
    return
  fishka(n-1)
  print(n, -(n-1), end=' ')


