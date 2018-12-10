import re
from node import Node


def part_two(input):
    structure = list(map(int, re.findall(r'(\d+)\b', input)))

    root = Node(structure.pop(0), structure.pop(0))
    root.process(structure)

    return root.value()


test_two = '2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2'

assert part_two(test_two) == 66

with open('input.txt') as file:
    input = file.readline().strip()

print('Root value: ' + str(part_two(input)))
