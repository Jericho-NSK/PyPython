a = input().lower().replace('a', '1').replace('b', '2').replace('c', '3').replace('d', '4').replace('e', '5').replace(
    'f', '6').replace('g', '7').replace('h', '8')
b = input().lower().replace('a', '1').replace('b', '2').replace('c', '3').replace('d', '4').replace('e', '5').replace(
    'f', '6').replace('g', '7').replace('h', '8')
x1 = int(a[0])
y1 = int(a[1])
x2 = int(b[0])
y2 = int(b[1])
z = 0
if x1 != x2 or y1 != y2:
    if x1 != x2 and y1 == y2 or y1 != y2 and x1 == x2:
        print('Rook')
        z = 1
    if abs(x2 - x1) == abs(y2 - y1) and x1 != x2:
        print('Bishop')
        z = 1
    if abs(x2 - x1) == 1 and abs(y2 - y1) == 2 or abs(x2 - x1) == 2 and abs(y2 - y1) == 1:
        print('Knight')
        z = 1
    if (x1 != x2 and y1 == y2 or y1 != y2 and x1 == x2) or (abs(x2 - x1) == abs(y2 - y1) and x1 != x2):
        print('Queen')
        z = 1
    if 0 <= x2 - x1 <= 1 and 0 <= y2 - y1 <= 1:
        print('King')
        z = 1
    if (y1 == 2 and x1 == x2 and 1 <= y2 - y1 <= 2) or (y1 != 2 and x1 == x2 and y2 - y1 == 1):
        print('Pawn')
        z = 1
    if z == 0:
        print('Nobody')
else:
    print('Nobody')
