from collections import defaultdict


# Track overlaps between rectangles.
class Overlaps:
    def __init__(self):
        self.overlaps = defaultdict(lambda: set())
        self.claims = set()

    def __contains__(self, claim):
        return claim in self.claims

    def add(self, row: int, columns: int, claims: set):
        self.overlaps[row] |= columns
        self.claims |= claims

    def count(self) -> int:
        count = 0
        for row, columns in self.overlaps.items():
            count += len(columns)
        return count
