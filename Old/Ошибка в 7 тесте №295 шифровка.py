# n = input()
# k = input()
n = 'JNQPTTJCMFC'
k = 'IMPOSSIBLEA'
a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXY'
x = []
z = 0
for i in n:
    x.append(i)
while k not in n and z < 25:
    for i in range(len(n)):
        x.append(a[a.index(n[i]) + 1])
    del x[:len(n)]
    n = ''.join(x)
    z += 1
if k in n:
    print(n)
else:
    print('IMPOSSIBLE')
