import re


# Represents a rectangular claim from a larger piece of fabric.
class Claim:
    def __init__(self, id, left, top, width, height):
        self.id = int(id)
        self.left = int(left)
        self.top = int(top)
        self.width = int(width)
        self.height = int(height)

    def __str__(self):
        return '#{0} @ {1},{2}: {3}x{4}'.format(self.id, self.left, self.top,
                                                self.width, self.height)

    def overlaps(self, claim, overlaps):
        comparision = claim.ranges()
        overlap = False
        for row, columns in self.ranges().items():
            if row in comparision:
                intersection = set(columns).intersection(comparision[row])
                if len(intersection) > 0:
                    overlap = True
                    overlaps.add(row, intersection, set([self, claim]))

        return overlap

    def ranges(self):
        ranges = {}
        for row in range(self.top, self.top + self.height):
            ranges[row] = range(self.left, self.left + self.width)
        return ranges


    @classmethod
    def from_string(cls, string: str):
        matches = re.findall(r'^#(\d+) @ (\d+),(\d+): (\d+)x(\d+)$', string)
        if len(matches) == 0:
            raise ValueError('String "' + string + '" is not a valid format.')

        match = matches[0]
        return cls(match[0], match[1], match[2], match[3], match[4])
