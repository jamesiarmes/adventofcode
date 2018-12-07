from event import Event
from guard import Guard
from shift import Shift
from collections import defaultdict

with open('input.txt') as file:
    events = file.readlines()
    events = [Event.from_string(x.strip()) for x in events]
    events.sort(key=lambda x: x.time)

guards = defaultdict(lambda: None)
for event in events:
    if event.type() == 'identifier':
        shift = Shift(event.time)
        guard_id = event.guard_id()
        guard = guards[guard_id]
        if not guard:
            guard = Guard(event.guard_id())
            guards[guard_id] = guard
        guard.add_shift(shift)
    elif event.type() == 'sleeping':
        shift.sleep(event.time)
    else:
        shift.wake(event.time)

max_sleep = 0
max_sleep_guard = None
max_sleep_minute = None
for _, guard in guards.items():
    analysis = guard.analyze()
    if analysis['total_sleep'] > max_sleep:
        max_sleep = analysis['total_sleep']
        max_sleep_minute = analysis['minute_most_asleep']
        max_sleep_guard = guard

print('Guard: #' + str(max_sleep_guard.id))
print('Total sleep: ' + str(max_sleep))
print('Most slept minute: ' + str(max_sleep_minute))
print('Result: ' + str(max_sleep_guard.id * max_sleep_minute))

