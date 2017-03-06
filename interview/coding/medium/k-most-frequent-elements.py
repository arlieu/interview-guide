'''Given an array of values, find the k most frequent elements.'''


def kFrequentElements(A, k):
    char_count = {}
    for i in A:
        if i in char_count:
            char_count[i] += 1
        else:
            char_count[i] = 1

    res = list(sorted(char_count, key=char_count.get, reverse=True))
    return res[:k]