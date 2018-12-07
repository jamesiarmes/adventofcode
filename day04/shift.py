import datetime


# Represents a guard shift.
class Shift:
    def __init__(self, start: datetime):
        if start.hour == 23:
            start += datetime.timedelta(minutes=(60 - start.minute))
        self.start = start
        self.state = 'awake'
        self.updated = start.minute
        self.sleeping = []

    def sleep(self, time: datetime):
        self.state = 'sleeping'
        self.updated = time.minute

    def wake(self, time: datetime):
        self.state = 'awake'
        self.sleeping += list(range(self.updated, time.minute))
        self.updated = time.minute

    def time_sleeping(self):
        return len(self.sleeping)
