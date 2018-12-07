from collections import defaultdict
from collections import namedtuple
import operator


# Represents a guard.
class Guard:
    def __init__(self, id):
        self.id = id
        self.events = []
        self.days = defaultdict(lambda: {'events': []})
        self.shifts = []

    def add_shift(self, shift):
        self.shifts.append(shift)

    def analyze(self):
        total_sleep = 0
        times_asleep = []
        for shift in self.shifts:
            total_sleep += shift.time_sleeping()
            times_asleep += shift.sleeping

        minute_most_asleep = defaultdict(lambda: None)
        if total_sleep > 0:
            minute_most_asleep = self._find_minute_most_asleep(times_asleep)

        return {
            'total_sleep': total_sleep,
            'minute_most_asleep': minute_most_asleep['minute'],
            'days_asleep_at_minute': minute_most_asleep['days'],
        }

    def _find_minute_most_asleep(self, times_asleep):
        days_asleep_per_minute = defaultdict(int)
        for minute in times_asleep:
            days_asleep_per_minute[minute] += 1

        max_minute =  max(days_asleep_per_minute.items(),
                          key=operator.itemgetter(1))[0]

        return {
            'minute': max_minute,
            'days': days_asleep_per_minute[max_minute],
        }

