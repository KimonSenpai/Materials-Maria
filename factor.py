
n = int(input())
#24 = 2**3 * 3**1

div = 2
while div*div <= n:
  cnt = 0
  while n % div == 0:
    n //= div
    cnt += 1
  if cnt > 0:
    print (div, cnt)
  div += 1

if n > 1:
  print(n, 1)

