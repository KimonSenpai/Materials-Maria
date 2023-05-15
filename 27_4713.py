for file in ('27A_4713.txt', '27B_4713.txt'):
    f = open(file)

    n = int(f.readline())

    x = []
    cont = []

    for line in f:
        a, b = map(int, line.split())
        x += [a]
        cont += [b//36 + (b%36 > 0)]
    l_count, r_count = cont[0], 0
    l_cost, r_cost = 0, 0

    for i in range(1, n):
        r_count += cont[i]
        r_cost += cont[i]*(x[i] - x[0])
    
    min_cost = l_cost + r_cost

    for i in range(1, n):
        l_cost += l_count*(x[i] - x[i-1])
        r_cost -= r_count*(x[i] - x[i-1])

        l_count += cont[i]
        r_count -= cont[i]

        min_cost = min(min_cost, l_cost + r_cost)

    print(min_cost)

