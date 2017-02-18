def bucketSort(array):
    maxValue = max(array)
    minValue = min(array)
    nBuckets = int((len(array)**(1/2)))
    buckets = [[]*nBuckets]

    for i in range(0, len(array)):
        buckets[((array[i]-minValue)%nBuckets)-1].append(array[i])

    resArray = []

    for i in buckets:
        insertionSort(i)
        for j in i:
            resArray.append(j)

    return resArray


def insertionSort(array):
    for i in range(1, len(array)):
        j = i

        while (j > 0) and (array[j-1] > array[j]):
            array[j], array[j-1] = swap(array[j], array[j-1])
            j -= 1


def swap(x, y):
    return y, x