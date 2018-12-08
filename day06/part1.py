from point import Point
from grid import Grid
from collections import Counter
from collections import defaultdict


def part_one(input):
    grid = Grid([Point.from_string(x.strip()) for x in input])

    grid = grid.build()
    exclude = set()
    for d in grid[0]:
        exclude.add(d)

    for d in grid[-1]:
        exclude.add(d)

    for line in grid:
        exclude.add(line[0])
        exclude.add(line[-1])

    sym = defaultdict(int)
    for line in grid:
        for c in line:
            if c in exclude:
                continue
            sym[c] += 1
    return sym[max(sym, key=lambda v: sym[v])]+1


test_one = [
    '1, 1',
    '1, 6',
    '8, 3',
    '3, 4',
    '5, 5',
    '8, 9',
]

assert part_one(test_one) == 17

with open('input.txt') as file:
    input = file.readlines()

print('Size of largest area: ' + str(part_one(input)))
