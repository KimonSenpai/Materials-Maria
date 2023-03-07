N = int(input())
k1, k2, k7, k14 = 0, 0, 0, 0
ans = 0
for i in range(N):
    val = int(input())
    if val % 14 == 0:
        ans = max(ans, val*k1, val*k2, val*k7, val*k14)
        k14 = max(k14, val)
    elif val % 7 == 0:
        ans = max(ans, val*k2, val*k14)
        k7 = max(k7, val)
    elif val % 2 == 0:
        ans = max(ans, val*k7, val*k14)
        k2 = max(k2, val)
    else:
        ans = max(ans, val*k14)
        k1 = max(k1, val)

print(ans)