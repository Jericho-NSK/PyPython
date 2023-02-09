x = 0
for i in range(35, -1, -1):
    y = x
    x += int((0.1 * i) ** 2) - 1
    print(35 - i, y)
