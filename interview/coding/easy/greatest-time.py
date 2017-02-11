'''Find the greatest military time that can be created from four digits.'''


def greatestTime(A, B, C, D):
    tmp = [A, B, C, D]

    hour0 = None
    for i in tmp:
        if i <= 2 and (hour0 is None or i > hour0):
            hour0 = i

    if hour0 is None:
        return "NO VALID TIME"

    tmp.remove(hour0)

    hour1 = None
    for i in tmp:
        if hour0 == 2:
            if i <= 4 and (hour1 is None or i > hour1):
                hour1 = i
        else:
            if hour1 is None or i > hour1:
                hour1 = i

    if hour1 is None:
        return "NO VALID TIME"

    tmp.remove(hour1)

    min0 = None
    for i in tmp:
        if i <= 5 and (min0 is None or i > min0):
            min0 = i

    if min0 is None:
        return "NO VALID TIME"

    tmp.remove(min0)

    min1 = None
    for i in tmp:
        if min1 is None or i > min1:
            min1 = i

    if min1 is None:
        return "NO VALID TIME"

    return str(hour0) + str(hour1) + ":" + str(min0) + str(min1)