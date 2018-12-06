from claim import Claim
from overlaps import Overlaps

with open('input.txt') as file:
    claims = file.readlines()
    claims = [Claim.from_string(x.strip()) for x in claims]

overlaps = Overlaps()
for index, claim in enumerate(claims):
    overlap = False
    for comparision in claims[(index + 1):]:
        claim.overlaps(comparision, overlaps)

print('Total overlaps: ' + str(overlaps.count()))

