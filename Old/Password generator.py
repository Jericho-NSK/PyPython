# в пароле должно быть хотя бы A заглавных букв;
# в пароле должно быть хотя бы B строчных букв;
# в пароле должно быть хотя бы C цифр;
# в пароле не должно быть двух одинаковых идущих подряд символов.
from random import randint as r
from random import shuffle as s
from string import printable as p

# n = int(input()) # Всего символов
# a, b, c = map(int, input().split()) # Заглавные, строчные, цифры
n, a, b, c = 8, 2, 5, 3 # Всего символов, заглавные, строчные, цифры
k = 0
z = []
for i in range(n):
    while a > 0:
        z.append(p[r(p.index('A'), p.index('Z'))])
        a -= 1
    while b > 0:
        z.append(p[r(p.index('a'), p.index('z'))])
        b -= 1
    while c > 0:
        z.append(p[r(p.index('0'), p.index('9'))])
        c -= 1
    while len(z) < n:
        z.append(p[r(p.index('0'), p.index('Z'))])
s(z)
while k > 0:
    k = 0
    for i in range(1, len(z)):
        if z[i] == z[i-1]:
            k += 1
            s(z)
print(''.join(z))
