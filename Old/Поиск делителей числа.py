n = 100
b = []
for j in range(n):
    i = 2
    a = []
    while i * i <= j:
        if j % i == 0:
            a.append(i)
            if i != j // i:
                a.append(j // i)
        i += 1
    a = sorted(a)
    if len(a) > 9:
        b.append(a)
        b.append(j)
for i in range(1, len(b), 2):
    print(b[i], len(b[i - 1]), b[i-1])
print(int(len(b) / 2))
