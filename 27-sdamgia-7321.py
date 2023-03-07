
N = int(input())
t = int(input())

A, B = 0, t

for i in range(N):
    a, b = map(int, input().split())
    A = A + a
    B = min(A + t, B + b)

print(B)