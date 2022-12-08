f = open(R"D:\Downloads\17 (5).txt", 'r')


mas = [int(line) for line in f]

cnt = 0
max_sum = -100000

for i in range(1, len(mas)):
  if mas[i] % 3 == 0 or mas[i - 1] % 3 == 0:
    cnt += 1
    max_sum = max(max_sum, mas[i] + mas[i - 1])

print(cnt, max_sum)