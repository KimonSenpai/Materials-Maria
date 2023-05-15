f=  open('24_7600.txt')

s = f.readline() + '#'

ln = 0
max_ln = 0

prev = 'A'

for c in s:
    if c == '#' or c == prev == '@':
        max_ln = max(max_ln, ln)
        ln = 1
    else:
        ln += 1

    prev = c

print(max_ln)