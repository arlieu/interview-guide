def selectionSort(array):
    for i in range(0, len(array)):
        tmpMin = i

        for j in range(i+1, len(array)):
            if array[j] < array[tmpMin]:
                tmpMin = j

        if tmpMin != i:
            array[tmpMin], array[i] = swap(array[tmpMin], array[i])

    return array


def swap(x, y):
    return y, x