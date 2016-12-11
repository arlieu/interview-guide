def heapsort(array):
    length = len(array)-1
    parent = length//2

    for i in range(parent, -1, -1):
        shift(array, i, length)

    for i in range(length, 0, -1):
        if array[0] > array[i]:
            array[0], array[i] = swap(array[0], array[i])
            shift(array, 0, i-1)


def shift(array, first, last):
    greatest = 2*first+1

    while greatest <= last:
        if greatest < last and array[greatest] < array[greatest+1]:
            greatest += 1

        if array[greatest] > array[first]:
            array[greatest], array[first] = swap(array[greatest], array[first])
            first = greatest
            greatest = 2*first+1

        else:
            return


def swap(x, y):
    return y, x