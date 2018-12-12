from grid import Grid


def part_two(serial_number):
    grid = Grid(serial_number)
    grid.build()

    max_area = None
    best_size = 0
    for size in range(1, 301):
        area = grid.find_highest_power_area(size)
        if max_area is None or area.power > max_area.power:
            best_size = size
            max_area = area

    return str(max_area.start.x) + ',' + str(max_area.start.y) + ',' \
        + str(best_size)


# This takes a while, so comment these out to only run against the actual input.
# Also recommended to run via pypy.
# assert part_two(18) == '90,269,16'
# assert part_two(42) == '232,251,12'

with open('input.txt') as file:
    input = file.readline().strip()

area = part_two(int(input))
print(area)
