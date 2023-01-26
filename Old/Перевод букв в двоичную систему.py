# Когда Серёже было три года, ему подарили на день рождения набор карточек с буквами.
# С их помощью было записано словами любимое число мамы мальчика в двоичной системе счисления.
# Серёжа тотчас же принялся с ними играть, но так как не умел читать, перемешал их в случайном порядке.
# Папа решил привести в порядок карточки.
# Помогите ему восстановить исходное число при условии, что оно было максимально возможным.
import random

k = 10
lst = ['o', 'z', 'e', 'r', 'n']
letter = random.choices(lst, k=k)
one, zero = 0, 0
a = ''.join(letter)
# a = 'zzeoznneerreoznoernrororerzrrernrozzzzzzerneozzeonrerreezonorronzrezneeozezerrrzrrroeezooonznoneeenr'
print(a)
while a.find('n') != -1 and a.find('o') != -1 and a.find('e') != -1:
    o = a.find('o')
    a = a.replace('o', '', 1)
    n = a.find('n')
    a = a.replace('n', '', 1)
    e = a.find('e')
    a = a.replace('e', '', 1)
    one = one + 1
while a.find('z') != -1 and a.find('e') != -1 and a.find('r') != -1 and a.find('o') != -1:
    z = a.find('z')
    a = a.replace('z', '', 1)
    e = a.find('e')
    a = a.replace('e', '', 1)
    r = a.find('r')
    a = a.replace('r', '', 1)
    o = a.find('o')
    a = a.replace('o', '', 1)
    zero = zero + 1
text = '1' * one + '0' * zero
print(text.replace('', ' '))
