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
    def __init__(self, curve, x, y, infinity=False):
        self.x = x
        self.y = y
        self.curve = curve
        self.is_infinity = infinity
        if not infinity and not curve.contains(self):
            raise Exception('Point ({}, {}) does not lie on curve y**2 = x**3 + {}x + {}'.format(x, y, self.curve.a, self.curve.b))

    def __add__(self, p1):
        if p1.x == self.x and p1.y == self.y: return self.double()
        if self.is_infinity:return p1
        elif p1.is_infinity: return self

        dx = self.x - p1.x
        dy = self.y - p1.y
        inv_dx = extendedEuclid(dx, self.curve.p)[0]
        slope = (dy * inv_dx) % self.curve.p

        x = (slope **2 - self.x - p1.x ) % self.curve.p
        y =  (slope * (self.x - x) - self.y) % self.curve.p
        return Point(self.curve, x, y)
        return self._get_reflected_point_from_dy_dx(dy, dx)


    def double(self):
        if self.is_infinity:
            return self
        # get x and y
        dx = 2*self.y
        dy = 3*self.x**2 + self.curve.a

        inv_dx = extendedEuclid(dx, self.curve.p)[0]
        slope = (dy * inv_dx) % self.curve.p

        x = (slope **2 - 2*self.x ) % self.curve.p
        y =  (slope * (self.x - x) - self.y) % self.curve.p
        return Point(self.curve, x, y)


    def __str__(self):
        return "Point: ({}, {})".format(self.x, self.y)

    def __rmul__(self, n):
        return self.__mul__(n)

    def __mul__(self, n):
        p = Point(self.curve, 0, 0, True)
        p0 = Point(self.curve, self.x, self.y)
        while n:
            r = n%2
            n = n/2
            if r == 1:
                p = p + p0
            p0 = p0.double()
        return p


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
    prime = 2**256 - 2**32 - 2**9 - 2**8 - 2**7 - 2**6 - 2**4 - 1
    Gx = 55066263022277343669578718895168534326250603453777594175500187360389116729240
    Gy = 32670510020758816978083085130507043184471273380659243275938904335757337482424
    n = 1234
    curve = Curve(a=0, b=7,p=prime)
    point = Point( curve, Gx, Gy)
    print(n*point)
