for file in ('27A_7603.txt', '27B_7603.txt'):
    f = open(file)

    n = int(f.readline())
    k = int(f.readline())
    mas = [int(line) for line in f]

    max_val = -10**9
    max_sum = -10**9

    for i in range(k, n):
        max_val = max(max_val, mas[i-k])
        max_sum = max(max_sum, mas[i] + max_val)

    print(max_sum)
