'''Find the first repeating character in a string.'''
def firstRepeat(s):
    dict1 = {}
    for i in s:
        if i not in dict1:
            dict1[i] = 1

        else:
            dict1[i] += 1

    index = None
    for i in range(len(s)):
        if dict1[s[i]] > 1:
            if index is None or index > i:
                index = i

    if index is None:
        return None

    return s[index]