a = {'a': ['a', 'b'], 'b': [1, 2]}
b = {'a': ['a', 'B'], 'c': [3, '4']}
c = {'a': ['A', 'b'], 'c': [3, 4]}

# c = {key: values + b[key] for key, values in a}
# print(c)

for key, value in b.items():
    if key in a:
        a[key] = list(set(a[key] + value))
    else:
        a[key] = value


for key, value in c.items():
    if key in a:
        a[key] = list(set(a[key] + value))
    else:
        a[key] = value

print(a)

from collections import defaultdict
d = defaultdict(lambda: 'default')
d['key'] = 'value'

print(d['key'])
print(d[0])
