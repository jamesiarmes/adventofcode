import operator
from point import Point

class Grid:
    def __init__(self, points=[]):
        self.points = points
        for point in points:
            point.grid = self

    def right(self):
        return max(self.points, key=operator.attrgetter('x')).x

    def left(self):
        return min(self.points, key=operator.attrgetter('x')).x

    def bottom(self):
        return max(self.points, key=operator.attrgetter('y')).y

    def top(self):
        return min(self.points, key=operator.attrgetter('y')).y

    def build(self):
        grid = []
        for x in range(self.right() + 1):
            grid.append([])
            for y in range(self.bottom() + 1):
                grid[x].append([])
                min_distance = None
                min_point = None
                for i, point in enumerate(self.points):
                    distance = point.distance(Point(x, y))
                    if min_distance is None or distance < min_distance:
                        min_distance = distance
                        min_point = i
                    elif distance == min_distance:
                        min_point = '.'

                    if distance == 0:
                        min_point = '*'

                grid[x][y] = str(min_point)

        return grid

