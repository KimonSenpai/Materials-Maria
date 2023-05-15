f = open(R"26_8432.txt", 'r')
n = int(f.readline())
mas_A = [0]*70
mas_B = [0]*30
cnt_B, cnt_A = 0, 0
mas = []
nmas = []
for i in range(1, n + 1):
    a, b, c = map(str, f.readline().split())
    mas += [(int(a), 1, c, i)]
    mas += [(int(b)+int(a), 0, c, i)]
mas.sort()
for a, b, c, d in mas:
    if c == 'B':
        if b == 1:
            for i in range(30):
                if mas_B[i] == 0:
                    mas_B[i] = d
                    cnt_B += 1
                    cnt_A -= 1
                    break
            cnt_A += 1
        else:
            for i in range(30):
                if mas_B[i] == d:
                    mas_B[i] = 0
    else:
        if b == 1:
            f = False
            for i in range(70):
                if mas_A[i] == 0:
                    mas_A[i] = d
                    
                    f = True
                    break
            if not f:
                for i in range(30):
                    if mas_B[i] == 0:
                        mas_B[i] = d
                        f = True
                        break
            if not f: cnt_A += 1
        else:
            for i in range(30):
                if mas_B[i] == d:
                    mas_B[i] = 0
            for i in range(70):
                if mas_A[i] == d:
                    mas_A[i] = 0

print(cnt_B, cnt_A)