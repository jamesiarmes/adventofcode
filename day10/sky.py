import operator


class Sky:
    def __init__(self, points):
        self.points = points
        self.x_range = range(self.left(), self.right() + 1)
        self.y_range = range(self.top(), self.bottom() + 1)

    def right(self):
        return max(self.points, key=operator.attrgetter('x')).x

    def left(self):
        return min(self.points, key=operator.attrgetter('x')).x

    def bottom(self):
        return max(self.points, key=operator.attrgetter('y')).y

    def top(self):
        return min(self.points, key=operator.attrgetter('y')).y

    def size(self):
        return (self.right() - self.left()) * (self.bottom() - self.top())

    def lapse_time(self, seconds):
        for point in self.points:
            point.move(seconds)

    def visualize(self):
        sky = {}
        for y in range(self.top(), self.bottom() + 1):
            sky[y] = {}
            for x in range(self.left(), self.right() + 1):
                sky[y][x] = ' '

        for point in self.points:
            sky[point.y][point.x] = '#'

        return sky
