from polymer import Polymer

with open('input.txt') as f:
    polymer = Polymer(f.readline().strip())

min_length = len(polymer.units)
for type in set(polymer.units.lower()):
    polymer.remove(type)
    length = len(polymer.react())
    if length < min_length:
        min_length = length

    polymer.reset()

print('Minimum length: ' + str(min_length))
