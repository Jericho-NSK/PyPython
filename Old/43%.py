'''Задана формула следующего вида:
<формула> ::=<цифра>|M(<формула>,<формула>)|m(<формула>,<формула>)
<цифра> ::= 0|1|2|3|4|5|6|7|8|9
где М обозначает функцию max – максимальный элемент, m обозначает функцию min – минимальный элемент, | - знак «или».
Требуется вычислить значение по данной формуле'''
def rec(n):
    if 'm' in n and 'M' in n and n.rindex('m') > n.rindex('M'):
        a = n[:n.rindex('m')]
        b = int(n[n.rindex('m') + 2:n.index(',', n.rindex('m'))])
        c = int(n[n.index(',', n.rindex('m')) + 1:n.index(')', n.rindex('m'))])
        d = str(min(b, c))
        e = n[n.index(')', n.rindex('m')) + 1:]
        return rec(a + d + e)
    if 'm' in n and 'M' in n and n.rindex('m') < n.rindex('M'):
        a = n[:n.rindex('M')]
        b = int(n[n.rindex('M') + 2:n.index(',', n.rindex('M'))])
        c = int(n[n.index(',', n.rindex('M')) + 1:n.index(')', n.rindex('M'))])
        d = str(max(b, c))
        e = n[n.index(')', n.rindex('M')) + 1:]
        return rec(a + d + e)
    if 'm' in n and 'M' not in n:
        while 'm' in n:
            a = n[:n.rindex('m')]
            b = int(n[n.rindex('m') + 2:n.index(',', n.rindex('m'))])
            c = int(n[n.index(',', n.rindex('m')) + 1:n.index(')', n.rindex('m'))])
            d = str(min(b, c))
            e = n[n.index(')', n.rindex('m'))+1:]
            n = a + d + e
    if 'M' in n and 'm' not in n:
        while 'M' in n:
            a = n[:n.rindex('M')]
            b = int(n[n.rindex('M') + 2:n.index(',', n.rindex('M'))])
            c = int(n[n.index(',', n.rindex('M')) + 1:n.index(')', n.rindex('M'))])
            d = str(max(b, c))
            e = n[n.index(')', n.rindex('M'))+1:]
            n = a + d + e
    if n.isdigit():
        return n


n = input()
# n = 'M(5,m(6,8))'
if n[0].isdigit():
    print(n[0])
else:
    print(rec(n))
    # print(n[n.index(',', n.rindex('m')) + 1:n.index(')', n.rindex('m'))])

