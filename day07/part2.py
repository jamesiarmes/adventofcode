from instructions import Instructions
from worker import Worker


def part_two(input, workers_count, base_time):
    instructions = Instructions()
    instructions.steps_from_strings(input)

    for worker_id in range(1, workers_count + 1):
        instructions.add_worker(Worker(worker_id))

    return instructions.work(base_time)


test_one = [
    'Step C must be finished before step A can begin.',
    'Step C must be finished before step F can begin.',
    'Step A must be finished before step B can begin.',
    'Step A must be finished before step D can begin.',
    'Step B must be finished before step E can begin.',
    'Step D must be finished before step E can begin.',
    'Step F must be finished before step E can begin.',
]

assert part_two(test_one, 2, 0) == 15

with open('input.txt') as file:
    input = file.readlines()

print('Seconds to complete: ' + str(part_two(input, 5, 60)))
