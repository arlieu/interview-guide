def bubblesort(array):
    for i in range(0, len(array)):
        for j in range(0, len(array)):
            if array[j] > array[i]:
                array[i] += array[j]
                array[j] = array[i] - array[j]
                array[i] -= array[j]

    return array