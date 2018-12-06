from claim import Claim
from overlaps import Overlaps

with open('input.txt') as file:
    claims = file.readlines()
    claims = [Claim.from_string(x.strip()) for x in claims]

overlaps = Overlaps()
for index, claim in enumerate(claims):
    for comparision in claims[(index + 1):]:
        claim.overlaps(comparision, overlaps)

    # We know that there is only one claim with no overlaps, so once we find it
    # we can stop.
    if claim not in overlaps:
        print('Intact claim: ' + str(claim))
        break

