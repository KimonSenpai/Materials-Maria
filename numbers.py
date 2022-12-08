from math import ceil

mas = []
n = int(input())
count = 0
for a1 in range(2, 10):
  for a2 in range(ceil(100/(9*a1)), 10):
    for a3 in range(ceil(100/(a1*a2)), 10):
      mas += [100*a1 + 10*a2 + a3]
      count += 1
      if count == n: break
    
    if count == n: break
  
  if count == n: break

print(*mas[:n])

