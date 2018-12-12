from collections import namedtuple
from power_cell import PowerCell


class Grid:
    def __init__(self, serial_number):
        self.serial_number = serial_number
        self.grid = {}

    def __getitem__(self, item):
        return self.grid[item]

    def build(self):
        for x in range(1, 301):
            self.grid[x] = {}
            for y in range(1, 301):
                self.grid[x][y] = PowerCell(x, y, self.serial_number)

    def find_highest_power_area(self, size):
        max_power = 0
        area_start = None
        for x in range(1, 301 - size):
            for y in range(1, 301 - size):
                total_power = 0
                for area_x in range(size):
                    for area_y in range(size):
                        total_power += self.grid[x + area_x][y + area_y].power_level()

                if total_power > max_power:
                    max_power = total_power
                    area_start = self.grid[x][y]

        area = namedtuple('MaxPowerArea', ('power', 'start'))
        area.power = max_power
        area.start = area_start

        return area

