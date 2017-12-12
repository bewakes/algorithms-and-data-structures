def extendedEuclid(m, n):
    r = m % n
    if r == 0: return (0, 1, n)
    a,b,g = extendedEuclid(n, r)
    q = int(m/n)
    return (b, -q*b + a, g)

class Curve:
    def __init__(self, a=0, b=7, p=7):
        self.a = a
        self.b = b
        self.p = p

    def contains(self, point):
        x = point.x
        y = point.y
        return (y**2 % self.p) == (x**3 + self.a*x + self.b) % self.p


class Point:
    def __init__(self, curve, x, y):
        self.x = x
        self.y = y
        self.curve = curve
        self.is_infinity = False
        if not curve.contains(self):
            raise Exception('Point ({}, {}) does not lie on curve y**2 = x**3 + {}x + {}'.format(x, y, self.curve.a, self.curve.b))

    def __add__(self, p1):
        if p1.x == self.x and p1.y == self.y: return self.double()
        if self.is_infinity:return p1
        elif p1.is_infinity: return self

        dx = self.x - p1.x
        dy = self.y - p1.y
        return self._get_reflected_point_from_dy_dx(dy, dx)


    def _get_reflected_point_from_dy_dx(self, dy, dx):
        inv_dx = extendedEuclid(dx, self.curve.p)[0]
        slope = (dy * inv_dx) % self.curve.p

        x = (slope **2 - 2*self.x ) % self.curve.p
        y =  (slope * (self.x - x) - self.y) % self.curve.p
        return Point(self.curve, x, y)

    def double(self):
        if self.is_infinity:
            return self
        # get x and y
        dx = 2*self.y
        dy = 3*self.x**2 + self.curve.a
        return self._get_reflected_point_from_dy_dx(dy, dx)


    def __str__(self):
        return "Point: ({}, {})".format(self.x, self.y)

    def __mul__(self, n):
        pass


def multiply(a, b):
    s = 0
    while b:
        r = b%2
        b = b/2
        if r == 1:
            s+=a
        a = a + a
    return s


if __name__ == '__main__':
    curve = Curve(a=2, b=3,p=97)
    point = Point( curve, 3, 6 )
    print(point)
    print(point+point)
    print(point+point+point)
