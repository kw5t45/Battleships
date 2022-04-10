def validate_ship_notation(notation):
    # Notation should only be in A3-A5 / B2-C2 form.

    if "-" not in notation:
        return False

    start_end_list = notation.split("-")
    start = start_end_list[0]
    end = start_end_list[1]

    if len(start) > 3:
        return False

    if start[0] not in "ABCDEFGHIJ" or start[1] not in "123456789":
        return False

    # if A10 case

    try:
        if start[1] == "1" and start[2] not in "0":
            return False
    except:
        pass

    # and for end notation

    if len(end) > 3:
        return False

    if end[0] not in "ABCDEFGHIJ" or end[1] not in "123456789":
        return False

    # if A10 case

    try:
        if end[1] == "1" and end[2] not in "0":
            return False
    except:
        pass

    if start[0] != end[0] and start[1] != end[1]:  # A1-B2 case
        return False

    # ships can be placed only horizontally or vertically <=>StartChar and EndChar must be the same (Vertical placement)
    # or StarNum and EndNum must be the same (Horizontal placement).

    if start[0] == end[0]:  # Vertical placement
        if start[1] >= end[1] and len(end) == 2:
            return False

    if start[1] == end[1]:  # Horizontal placement
        if start[0] >= end[0] and len(end) == 2:  # and ">" because B9-B10 case
            return False
    return True


def validate_single_notation(string):
    if len(string) > 3 or len(string) == 1:
        return False
    letters = 'ABCDEFGHJ'
    numbers = '123456789010'
    if string[0] not in letters or string[1::] not in numbers:
        return False
    return True
