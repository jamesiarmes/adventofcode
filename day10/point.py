import re


class Point:
    def __init__(self, x, y, velocity_x, velocity_y):
        self.x = x
        self.y = y
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y

    def move(self, seconds):
        self.x += self.velocity_x * seconds
        self.y += self.velocity_y * seconds

    @classmethod
    def from_string(cls, string):
        matches = re.findall(
            r'^position=<\s*(-?\d+),\s+(-?\d+)> '
            + r'velocity=<\s*(-?\d+),\s+(-?\d+)>$', string
        )
        if len(matches) == 0:
            raise ValueError('String "' + string + '" is not a valid format')

        match = matches[0]

        return cls(int(match[0]), int(match[1]), int(match[2]), int(match[3]))
