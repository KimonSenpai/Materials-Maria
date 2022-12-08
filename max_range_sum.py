n = int(input())

pref = 0
min_pref = 0
i = 1
res_i = res_j = 0
res_sum = -3*10^9 - 1

for j in range(1, n+1):
  val = int(input())
  pref += val
  if pref - min_pref > res_sum:
    res_i = i
    res_j = j
    res_sum = pref - min_pref
  if pref <= min_pref:
    min_pref = pref
    i = j + 1

print(res_i, res_j)

