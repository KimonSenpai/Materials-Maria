f = open('17-6353.txt')

mas = [int(line) for line in f]

mx = max([val for val in mas if val % 118 == 0 and abs(val)%10 != 8])

cnt, max_sum = 0, 0

for i in range(0, len(mas) - 2):
    trio = [mas[i], mas[i+1], mas[i+2]]

    if any(abs(val) % 1000 == 118 for val in trio) and any(val % 118 == 0 for val in trio) and sum(trio) > mx:
        cnt += 1
        max_sum = max(max_sum, sum(trio)**2)

print(cnt, max_sum)