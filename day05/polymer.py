import re


class Polymer:
    def __init__(self, units):
        self.units = units
        self.base = units

    def reset(self):
        self.units = self.base

    def remove(self, type):
        chars = [type, type.upper()]
        self.units = re.sub(r'[' + re.escape(''.join(chars)) + r']', '', self.units)

    def react(self):
        return self._reduce(self.units)

    def _reduce(self, string):
        result = string
        matches = re.finditer(r'(.)(?!\1)(?i:\1)', self.units)
        for match in matches:
            result = result.replace(match.group(0), '', 1)

        if result != string:
            result = self._reduce(result)

        return result
