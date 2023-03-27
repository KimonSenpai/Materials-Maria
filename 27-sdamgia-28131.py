for file in ("27_A (2).txt", "27_B (2).txt"):
    f = open(file)
    n = int(f.readline())
    mas = [-1]*120
    maxsum = 0
    ai = 0
    aj = 0
    for i in range(n):
        val = int(f.readline())
                 
        if mas[-val%120] > val:
            if val + mas[-val%120] > maxsum:
                maxsum = val + mas[-val%120]
                ai, aj = mas[-val%120], val
        mas[val%120] = max(mas[val%120], val)
    print(ai, aj)
