frequency = 0
frequencies = [0]
duplicate = None

inputs = []
with open('input.txt') as file:
    inputs = file.readlines()
    inputs = [x.strip() for x in inputs]

while duplicate is None:
    for x in inputs:
        operator = x[0]
        value = int(x[1:])
        if operator == '+':
            frequency += value
        elif operator == '-':
            frequency -= value

        if duplicate is None and frequency in frequencies:
            duplicate = frequency
            break
        frequencies.append(frequency)


print('First duplicate: ' + str(duplicate))
