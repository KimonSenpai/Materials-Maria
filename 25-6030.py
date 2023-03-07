
def gen_num(star_len, star, ques):
  return ((1203 + ques*10)*10**star_len + star)*100 + 46

for star_len in range(0, 3):
  for ques in range(0, 10):
    for star in range(0, 10**star_len):
      val = gen_num(star_len, star, ques)
      if val % 129 == 0:
        print(val, val//129)