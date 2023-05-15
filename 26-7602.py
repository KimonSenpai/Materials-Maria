f = open('26_7602.txt')

K = int(f.readline())

boxes = [0]*K

N = int(f.readline())

pas = []

for p in range(1, N+1):
    fr, to = map(int, f.readline().split())

    pas.append((fr, 1, p))
    pas.append((to + 1, 0, p))

pas.sort()

last_box = 0
cnt = 0

for time, inout, p in pas:
    if inout == 1:
        for i in range(len(boxes)):
            if boxes[i] == 0:
                boxes[i] = p
                cnt += 1
                last_box = i+1
                break
    else:
        for i in range(len(boxes)):
            if boxes[i] == p:
                boxes[i] = 0
                break
        
print(cnt, last_box)