class Shape:
    def __init__(self, a=10, b=6):
        self.set_params(a, b)

    def set_params(self, a, par_b):
        self._a = a
        self.b = par_b

    def get_a(self):
        return self._a

    def __repr__(self):
        return self.__class__.__name__ + "[" + str(self._a) + " by " + str(self.b) + "] at " + str(hex(id(self)))


class Rectangle(Shape):
    def calc_surface(self):
        return self._a*self.b

    def swap_sides(self):
        a = self._a
        b = self.b
        self._a = b
        self.b = a

#perimeter calculation to rectangle:
    def calc_perimeter(self):
        return (self._a + self.b) * 2

    def __repr__(self):
        return self.__class__.__name__ + "[" + str(self._a) + " by " + str(self.b) + "] at " + str(hex(id(self)))


import math

class Circle(Shape):
    def __init__(self, a):
        # call constructor of superclass (parent)
        super().__init__(a, 0)
        #self._a = a

    def calc_surface(self):
        return math.pi * self._a**2

    def __repr__(self):
        return self.__class__.__name__ + "[r=" + str(self._a) + "] at " + str(hex(id(self)))

#perimeter calculation to circle:
    def calc_perimeter(self):
        return self._a * math.pi * 2

    def __repr__(self):
        return self.__class__.__name__ + "[r=" + str(self._a) + "] at " + str(hex(id(self)))



a = None

# r = Rectangle(5, 6)
# print(r)
# #r._a = 600
# print(r.calc_surface())
# r.swap_sides()
# r_desc = str(r)
# print(r_desc)
#
# c = Circle(7)
# c_desc = str(c)
# print(c_desc)
# print(c.calc_surface())
# s = Sphere(8)
# print(s)
# print('s volume: ')
# print(s.calc_volume())
# print('s surface:')
# print(s.calc_surface())
#
# shape_list = [r, c, s]
# print()
# print('--------------------')
# for sh in shape_list:
#     print(sh.__class__.__name__)
#     sh.set_params(10, 15)
#     print(sh.calc_surface())

# adding Triangle:
class Triangle(Shape):
    def __init__(self, a, b, c):
       self.set_params(a, b, c)

    def set_params(self, a, b, c):
        self._a = a
        self.b = b
        self.c = c

    def calc_surface(self):
        s = (self._a + self.b + self.c) / 2
        return (s*(s-self._a)*(s-self.b)*(s-self.c)) ** 0.5
#perimeter calculation for triangle:
    def calc_perimeter(self):
        return self._a + self.b + self.c

    def __repr__(self):
        return self.__class__.__name__ + "[" + str(self._a) + ", " + str(self.b) + ", " + str(self.c)+ "] at " +str(hex(id(self)))

# adding Equilateral Triangle (inherits from Triangle) :
class EquilateralTriangle(Triangle):
    def __init__(self, a):
        super().__init__(a, a, a)


#perimeter calculation for EQUI triangle:
    def calc_perimeter(self):
        return self._a * 3

    def __repr__(self):
        return self.__class__.__name__ + "[" + str(self._a) + ", " + str(self._a) + ", " + str(self._a) + "] at " +str(hex(id(self)))

#ADDING Square (inherits from Rectangle):
class Square(Rectangle):
    def __init__(self, a):
        self._a = a
        self.b = a

    def __repr__(self):
        return self.__class__.__name__ + "[" + str(self._a) + "] at " + str(hex(id(self)))



# TESTS:
r = Rectangle(10, 56)
print(r)
print(r.calc_surface())
print(r.calc_perimeter())
print('--------------------')
c = Circle(9)
c_desc = str(c)
print(c_desc)
print(c.calc_surface())
print(c.calc_perimeter())
print('--------------------')
t = Triangle(1,2,3)
print(t)
print(t.calc_surface())
print(t.calc_perimeter())
print('--------------------')
e = EquilateralTriangle(9)
print(e)
print(e.calc_surface())
print(e.calc_perimeter())
print('--------------------')
s = Square(11)
print(s)
print(s.calc_surface())
print(s.calc_perimeter())