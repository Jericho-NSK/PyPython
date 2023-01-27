# Перестановки, факториал
def f(x):
    p = 1
    for i in range(2, x + 1):
        p *= i
    return p

# Перестановки с повторениями
def per():
    k = 1
    for i in range(len(set(n))):
        k *= f(n.count(list(set(n))[i]))
    return k

# Сочетания n по k
def sochet(n, k):
    return int(f(n) / (f(k) * f(n - k)))


# Размещения n по k
def rasm(n, k):
    return int(f(n) / f(n - k))


a, b = 10, 5
n = 'a'
print(sochet(max(a, b), min(a, b)))
print(rasm(max(a, b), min(a, b)))
print(int(f(len(n))/per()))
