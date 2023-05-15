for file in ("27-A_3231.txt", "27-B_3231.txt"):
    f = open(file)

    N = int(f.readline())

    mas = [int(val) for val in f]

    red_sum = green_sum = red_cost = green_cost = 0

    for i in range(1, N//2 + 1):
        green_sum += mas[i]
        green_cost += i*mas[i]
    for i in range(0, N//2):
        red_sum += mas[-i]
        red_cost += i*mas[-i]
    
    index, min_cost = 1, red_cost + green_cost

    for i in range(1, N):
      red_cost += red_sum - mas[(i + N//2) % N]*N//2
      green_cost += -green_sum + mas[(i + N//2) % N]*N//2
      red_sum += mas[i] - mas[(i + N//2) % N]
      green_sum += -mas[i] + mas[(i + N//2) % N]
      cost = red_cost + green_cost
      if cost < min_cost:
          min_cost = cost
          index = i + 1

    print(index)