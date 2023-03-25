

for file in ("28130_A.txt", "28130_B.txt"):
    f = open(file)
    N = f.readline()
    mas=[0]*80
    mas50=[0]*80
    cnt=0
    for val in f:
        val = int(val)
        if val>50:
            mas50[val%80]+=1
        else:
            mas[val%80]+=1
    for i in range(41):
        if i == -i%80:
            cnt += mas[i]*mas50[i] + (mas50[i]*(mas50[i] - 1)//2)
        else:
            cnt += mas[i]*mas50[-i%80] + mas50[i]*mas[-i%80] + mas50[i]*mas50[-i%80]
    print(cnt)
