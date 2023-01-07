class Qwe:
    def __str__(self):
        return 'text Qwe'
    # pass


# def f(cls):
#     print(cls.color)

Point2 = type('Point', (Qwe,), {'color': 'red'})
Point = type('Point', (Qwe,), {'color': 'red', '__repr__': lambda self: 'text'})
p = Point()
# print(p.f())
print(Point.__name__)
print(Qwe())