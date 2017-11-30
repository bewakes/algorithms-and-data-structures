def gcd(m, n):
    """
    Extended Euclidian algorithm to find a, b, g for integers m and n such that
    a*m + b*n = g, where g is the gcd of m and n
    PARAMS: m and n
    RETURNS: (a, b, g)
    """
    q = int(m/n)
    r = m % n
    if r == 0:
        return (0, 1, n)
    a,b,g = gcd(n, r)
    return (b*1, -q*b + a, g)

m = 2415
n = 3289
a, b, g = gcd(m, n)
print(a, b)
print(g)
print(a*m + b*n)
