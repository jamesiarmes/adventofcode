with open('input.txt') as file:
    ids = file.readlines()
    ids = [x.strip() for x in ids]

boxes = None
difference = None
difference_position = 0
for index, id in enumerate(ids):
    # Iterate over all of the ids on the list below the current one in order to
    # compare them. We don't need to compare the ones above because we already
    # have.
    for comparison in ids[index+1:]:
        difference_count = 0
        for position, char in enumerate(id):
            if comparison[position] is not char:
                difference_count += 1
                difference = char
                difference_position = position

                # If there's a difference of more than two characters then we
                # know there aren't our boxes and can move on to the next
                # comparison.
                if difference_count > 2:
                    break

        # If there's only a difference of one character then we've found the
        # boxes we're looking for.
        if difference_count == 1:
            boxes = [id, comparison]
            break

    # This would be much cleaner as a series of functions that could just return
    # rather then breaking multiple levels.
    if boxes is not None:
        break

if boxes:
    intersection = boxes[0][:difference_position] \
        + boxes[0][(difference_position + 1):]
    print('Intersection: ' + intersection)
