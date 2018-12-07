from polymer import Polymer

with open('input.txt') as f:
    polymer = Polymer(f.readline().strip())

print('Remaining units: ' + str(len(polymer.react())))

