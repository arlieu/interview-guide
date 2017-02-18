import math


def radixSort(array):
    maxLen = -1

    number = max(array)
    maxLen = int(math.log10(number))+1

    buckets = [[] for i in range(0, 10)]
    for digit in range(0, maxLen):
        for i in array:
            buckets[(i // 10**digit) % 10].append(i)
        del array[:]

        for bucket in buckets:
            array.extend(bucket)
            del bucket[:]

    return array