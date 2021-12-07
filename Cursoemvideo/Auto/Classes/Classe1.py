class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'


print(MyClass.f('Self'))
print(MyClass.i)

y = MyClass()
print(y.f())
print(y.i)


class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart


x = Complex(4, 5)
print(x.r, x.i)
