for file in ("27A_1977.txt", "27B_1977.txt"):
    f = open(file)
    n = int(f.readline())
    pref = [-1]*43
    pref_count = [0]*43
    pref[0] = 0
    i = 1
    s = 0
    max_sum = -1
    min_count = 10**30
    for line in f:
        val = int(line)
        s += val
        if pref[s % 43] == -1:
            pref[s % 43] = s
            pref_count[s % 43] = i
        else:
            summ = s - pref[s % 43]
            if summ > max_sum:
                max_sum = summ
                min_count = i - pref_count[s % 43]
            elif summ == max_sum:
                min_count = min(min_count, i - pref_count[s % 43])
        i += 1
    print(min_count)