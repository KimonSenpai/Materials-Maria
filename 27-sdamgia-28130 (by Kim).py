for file in ("28130_A.txt", "28130_B.txt"):
    f = open(file)
    N = f.readline()
    mas=[0]*80
    mas50=[0]*80
    cnt=0
    for val in f:
        val = int(val)
        if val>50:
            cnt += mas[-val%80] + mas50[-val%80]
            mas50[val%80]+=1
        else:
            cnt += mas50[-val%80]
            mas[val%80]+=1

    print(cnt)