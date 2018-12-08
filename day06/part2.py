from point import Point
from grid import Grid


def part_two(input, max_distance):
    grid = Grid([Point.from_string(x.strip()) for x in input])

    size = 0
    for x in range(grid.right() + 1):
        for y in range(grid.bottom() + 1):
            distances = [point.distance(Point(x, y)) for point in grid.points]
            if sum(distances) < max_distance:
                size += 1

    return size


test_two = [
    '1, 1',
    '1, 6',
    '8, 3',
    '3, 4',
    '5, 5',
    '8, 9',
]

assert part_two(test_two, 32) == 16

with open('input.txt') as file:
    input = file.readlines()

print('Region size: ' + str(part_two(input, 10000)))
