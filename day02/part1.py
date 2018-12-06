duplicates = []
triplicates = []

with open('input.txt') as file:
    ids = file.readlines()
    ids = [x.strip() for x in ids]

for id in ids:
    unique = set(id)
    for c in unique:
        count = id.count(c)
        if count == 2 and id not in duplicates:
            duplicates.append(id)
        elif count == 3 and id not in triplicates:
            triplicates.append(id)

checksum = len(duplicates) * len(triplicates)
print('Checksum: ' + str(checksum))
