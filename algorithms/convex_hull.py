import math


def distance(p1, p2):
    x1, y1, x2, y2 = [*p1, *p2]
    return ((x1-x2)**2 + (y1-y2)**2)**0.5


def is_clockwise(p1, p2, p3):
    s1 = angle(p1, p2)
    s2 = angle(p2, p3)
    return False if s2 >= s1 else True


def angle(p1, p2):
    x1, y1, x2, y2 = [*p1, *p2]
    if x1 == x2:
        if y1 > y2:
            return 3*math.pi/2
        return math.pi/2
    dy = y2-y1
    dx = x2-x1
    angle = math.atan(abs(dy)/abs(dx))
    if dx > 0 and dy > 0:
        return angle
    elif dx > 0 and dy <= 0:
        return 2*math.pi - angle
    elif dx < 0 and dy > 0:
        return math.pi - angle
    else:
        return math.pi + angle


def perimeter(polygon):
    return sum([
        distance(*x) for x in zip(polygon, polygon[1:] + [polygon[0]])
    ])


def direction_from_line(point, line):
    """
    @point: given point
    @line: two points, direction sensitive
    """
    # Direction given by y - y1 - (x-x1) * slope: equivalent to (ax + by + c)
    p1 = line[0]
    p2 = line[1]
    x1, y1, x2, y2, x, y = [*p1, *p2, *point]
    return (y-y1)*(x2-x1) - (x-x1)*(y2-y1)


def is_inside(point, convex_polygon):
    """
    @point: point in consideration
    @convex_polygon: list of adjacant points in polygon
    """
    direction = None
    for p1, p2 in zip(convex_polygon, convex_polygon[1:] + [convex_polygon[0]]):
        dir = direction_from_line(point, [p1, p2])
        if direction is None:
            direction = dir
        else:
            if direction * dir < 0:  # direction should always be same
                return False
    return True


def get_new_hull(hull, new_point):
    # recent directions
    prev = None
    curr = None
    lines = list(zip(hull, hull[1:]+[hull[0]]))
    for i, (p1, p2) in enumerate(lines):
        dir = direction_from_line(new_point, [p1, p2])
        if curr is None:
            curr = dir
        else:
            prev = curr
            curr = dir
            # NOTE: outside means direction -ve inside means direction +ve
            if prev >= 0 and curr < 0:  # Case outside, inside
                # Insert new point after current point
                return hull[:i+1] + [new_point] + hull[i+1:]
            elif prev <= 0 and curr <= 0:  # Case outside, outside
                # Replace the current point with new point
                return hull[:i] + [new_point] + hull[i+1:]
    return hull


def convex_hull(points):
    if len(points) <= 3:
        return points
    # Take 3 points, which is obviously a convex hull and use other points
    # to get a new convex hull
    hull = points[:3]
    # Check if it is anti clock wise
    if not is_clockwise(*hull):
        # reverse
        hull = [hull[0]] + hull[::-1][:-1]
    for x in points[3:]:
        hull = get_new_hull(hull, x)
    return hull


if __name__ == '__main__':
    n = int(input())
    points = []
    for x in range(n):
        inp = input()
        points.append([int(x) for x in inp.split()])
    hull = convex_hull(points)
    print(hull)
    print(perimeter(hull))
