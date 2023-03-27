
def xor(a, b):
    return bool((int(a) + int(b)) % 2)


for file in ("27-A_1786.txt", "27-B_1786.txt"):
    f = open(file)
    n = int(f.readline())
    mas = [[-1]*10 for _ in range(7)]

    mas[0][0] = 0

    for line in f:
        a, b, c = map(int, line.split())

        new_mas = [[-1]*10 for _ in range(7)]

        for s in (a + b, b + c, c + a):
            for i in range(7):
                for j in range(10):
                    if mas[i][j] == -1: continue
                    ii = (i + s)%7
                    jj = (j + s)%10

                    new_mas[ii][jj] = max(new_mas[ii][jj], mas[i][j] + s)
        mas = new_mas
    max_sum = -1
    for i in range(7):
        for j in range(10):
            if xor(i == 3, j == 5):
                max_sum = max(max_sum, mas[i][j])
    print(max_sum)