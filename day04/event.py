from datetime import datetime
import re


class Event:
    def __init__(self, time, message):
        self.time = time
        self.message = message

    def __str__(self):
        return '[{0}] {1}'.format(self.time.strftime('%Y-%m-%d %H:%M'),
                                  self.message)

    def type(self):
        matches = re.findall(r'^((?:Guard)|(?:falls asleep)|(?:wakes up))', self.message)
        switch = {
            'Guard': 'identifier',
            'falls asleep': 'sleeping',
            'wakes up': 'awake',
        }

        return switch.get(matches[0])

    def guard_id(self):
        matches = re.findall(r'^Guard #(\d+) ', self.message)
        if len(matches) == 0:
            raise ValueError('String "' + self.message +
                             '" is not a valid format')

        return int(matches[0])

    @classmethod
    def from_string(cls, string: str):
        matches = re.findall(r'^\[(.+?)\] (.+)$', string)
        if len(matches) == 0:
            raise ValueError('String "' + string + '" is not a valid format.')

        match = matches[0]
        time = datetime.strptime(match[0], '%Y-%m-%d %H:%M')

        return cls(time, match[1])
