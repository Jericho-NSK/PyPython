# n, k = map(str, input().split())
# n, k = '11', '2'
# a = 0
# for i in range(len(n)):
#     a += int(n[i]) * int(k) ** (len(n) - i - 1)
# print(a)


# n, k = map(str, input().split())
n, k = '100', '2'
n = int(n)
k = int(k)
x = []
while n > 0:
    x.append(str(n % k))
    n //= k
x.reverse()
if len(x) > 0:
    print(''.join(x))
else:
    print(0)