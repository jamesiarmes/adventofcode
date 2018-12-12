from grid import Grid


def get_cell(serial_number, x, y):
    grid = Grid(serial_number)
    grid.build()

    return grid[x][y]


def part_one(serial_number):
    grid = Grid(serial_number)
    grid.build()

    return grid.find_highest_power_area(3)


assert get_cell(8, 3, 5).power_level() == 4
assert get_cell(57, 122, 79).power_level() == -5
assert get_cell(39, 217, 196).power_level() == 0
assert get_cell(71, 101, 153).power_level() == 4

assert str(part_one(18).start) == '33, 45'
assert str(part_one(42).start) == '21, 61'


with open('input.txt') as file:
    input = file.readline().strip()

area = part_one(int(input))
print('Max power: ' + str(area.power))
print('Starting point: ' + str(area.start))
