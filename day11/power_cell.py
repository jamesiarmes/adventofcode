class PowerCell:
    def __init__(self, x, y, serial_number):
        self.x = x
        self.y = y
        self.serial_number = serial_number
        self.power = None

    def __str__(self):
        return str(self.x) + ', ' + str(self.y)

    def rack_id(self):
        return self.x + 10

    def power_level(self):
        if self.power:
            return self.power

        level = self.rack_id()
        level *= self.y
        level += self.serial_number
        level *= self.rack_id()
        level = int(str(level)[-3])
        level -= 5

        self.power = level

        return level

