

def move(a, b):
  return [f(a + 1, b), f(a, b + 1), f(a*2, b), f(a, b*2)]

m = {}
def f(a, b):
  if a+b >= 77:
    return -0
  global m
  if (a,b) in m: return m[(a, b)]
  mas = move(a, b)
  res = 0
  if all(val > 0 for val in mas):
    res= -(max(mas) + 1)
  else:
    res= -max(val for val in mas if val <= 0) + 1
  m[(a, b)] = res
  return res

print("problem 19")
for s in range(1, 69):
  if +1 in move(7, s):
    print(s)
    break

print("problem 20")
for s in range(1, 69):
  if f(7, s) == +3:
    print(s)

print("problem 21")
for s in range(1, 69):
  if f(7, s) == -4 and +1 in move(7, s):
    print(s)
    break


#a, b = b, a