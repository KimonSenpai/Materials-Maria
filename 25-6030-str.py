
def gen_num(star, ques):
  return int(f"12{ques}3{star}46")

stars = [""]
for star_len in range(1, 3):
  stars += [f"{val:0{star_len}}" for val in range(0, 10**star_len)]

res = []

for star in stars:
  for ques in range(0, 10):
    val = gen_num(star, ques)
    if val % 129 == 0:
      res += [val]

res.sort()
for val in res:
  print(val, val // 129)