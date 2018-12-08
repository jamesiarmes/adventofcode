class Point:
    def __init__(self, x: int, y: int, grid=None):
        self.x = x
        self.y = y
        self.grid = grid

    def __str__(self):
        return str(self.x) + ',' + str(self.y)

    def distance(self, point):
        return abs(self.x - point.x) + abs(self.y - point.y)

    def is_finite(self):
        return self.grid.left() < self.x < self.grid.right() \
          and self.grid.top() < self.y < self.grid.bottom()

    @classmethod
    def from_string(cls, string: str):
        x, y = string.split(', ')

        return cls(int(x), int(y))
