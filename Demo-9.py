
f = open("9.csv", 'r')

matr = [list(map(int, line.split(','))) for line in f]
res = 0
for line in matr:
  if len(set(line)) != 5: continue

  line.sort()
  sum_eq = 0
  sum_neq = 0
  i = 0
  while i < 6:
    if i == 5:
      sum_neq += line[i]
      i += 1
    elif line[i] == line[i+1]:
      sum_eq += 2*line[i]
      i += 2
    else:
      sum_neq += line[i]
      i += 1
  
  res += 1 if sum_neq/4 <= sum_eq else 0

print(res)