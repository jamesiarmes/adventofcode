from instructions import Instructions


def part_one(input):
    instructions = Instructions()
    instructions.steps_from_strings(input)

    return instructions.order()


test_one = [
    'Step C must be finished before step A can begin.',
    'Step C must be finished before step F can begin.',
    'Step A must be finished before step B can begin.',
    'Step A must be finished before step D can begin.',
    'Step B must be finished before step E can begin.',
    'Step D must be finished before step E can begin.',
    'Step F must be finished before step E can begin.',
]

assert part_one(test_one) == 'CABDFE'

with open('input.txt') as file:
    input = file.readlines()

print('Step order: ' + str(part_one(input)))

