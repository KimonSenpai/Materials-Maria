

x = [1, 2, 5, 2, 3]
y = [2, 5, 1, 5, 6]

print(list(zip(x, y, [1, 2, 3])))

print(list(map(lambda a: a**2, x)))

#I variant
s = 0
for i in range(len(x)):
  s += x[i]**2 + y[i]**2

#II variant
s = 0
for X, Y in zip(x, y):
  s += X**2 + Y**2

#III variant
s = sum(X**2 + Y**2 for X, Y in zip(x, y))


#"2 23 45" -split-> ["2", "23", "45"] -map-> [2, 23, 45]