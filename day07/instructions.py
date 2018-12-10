import re
from step import Step


class Instructions:
    def __init__(self):
        self.steps = {}
        self.workers = []

    def add_worker(self, worker):
        self.workers.append(worker)

    def steps_from_strings(self, step_strings: list):
        for s in step_strings:
            matches = re.findall(
                r'^Step ([A-Z]) must be finished before step ([A-Z]) can '
                + r'begin.$',
                s
            )
            if len(matches) == 0:
                raise ValueError('String "' + s + '" is not a valid format.')

            match = matches[0]
            if match[1] in self.steps:
                step = self.steps[match[1]]
            else:
                step = Step(match[1])
                self.steps[step.id] = step

            if match[0] in self.steps:
                dependency = self.steps[match[0]]
            else:
                dependency = Step(match[0])
                self.steps[dependency.id] = dependency

            step.add_dependency(dependency)

    def reset(self):
        for _, step in self.steps.items():
            step.status = Step.STATUS_WAITING

    def is_complete(self):
        for step in self.steps.values():
            if step.status != Step.STATUS_COMPLETE:
                return False

        return True

    def order(self):
        order = ''
        while not self.is_complete():
            step = self.next_step()
            step.complete()
            order += step.id

        self.reset()

        return order

    def work(self, base_time):
        seconds = 0
        while not self.is_complete():
            for worker in self.workers:
                if not worker.is_working(seconds):
                    next_step = self.next_step()
                    if next_step is None:
                        continue

                    complete_at = seconds + base_time + ord(next_step.id) - 64
                    worker.work_step(next_step, complete_at)

            if not self.is_complete():
                seconds += 1

        return seconds

    def next_step(self):
        next_step = None
        for id, step in self.steps.items():
            if step.status == Step.STATUS_WAITING and step.is_ready()\
               and (next_step is None or id < next_step.id):
                next_step = step

        return next_step

    def _next_step(self, remaining_steps: dict):
        next_step = None
        for id, step in remaining_steps.items():
            if step.is_ready() and (next_step is None or id < next_step.id):
                next_step = step

        next_step.complete()
        del(remaining_steps[next_step.id])

        return next_step
