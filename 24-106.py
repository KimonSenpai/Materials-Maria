

for val in range(135790, 163228 + 1):
  div = 2
  count = 0
  sum_div = 0
  while div*div <= val:
    if val % div == 0:
      count += 1
      sum_div += div
      if val//div != div:
        count += 1
        sum_div += val//div
    div += 1
  
  if sum_div > 460_000:
    print(count, sum_div)