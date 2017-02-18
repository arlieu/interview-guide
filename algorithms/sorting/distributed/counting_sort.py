def countingSort(array):
    upper = max(array)
    lower = min(array)

    countArr = [0]*(upper+1)

    for i in array:
        countArr[i] += 1

    for i in range(1, len(countArr)):
        countArr[i] += countArr[i-1]

    res = [None]*len(array)

    for i in array:
        index = countArr[i]
        countArr[i] -= 1
        res[index-1] = i

    return res