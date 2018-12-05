frequency = 0

inputs = []
with open('input.txt') as file:
    inputs = file.readlines()
    inputs = [x.strip() for x in inputs]

for x in inputs:
    operator = x[0]
    value = int(x[1:])
    if operator == '+':
        frequency += value
    elif operator == '-':
        frequency -= value

print('Frequency: ' + str(frequency))
