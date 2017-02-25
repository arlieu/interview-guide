'''Implement a merge sort.'''


def mergeSort(A):
    if len(A) == 0 or len(A) == 1:
        return A

    mid = len(A) // 2
    lA = A[:mid]
    uA = A[mid:]

    mergeSort(lA)
    mergeSort(uA)

    return merge(lA, uA, A)


def merge(lA, uA, A):
    i, j, k = 0, 0, 0
    while i<len(lA) and j<len(uA):
        if lA[i] < uA[j]:
            A[k] = lA[i]
            i+=1
        else:
            A[k] = uA[j]
            j+=1
        k+=1

    while i<len(lA):
        A[k] = lA[i]
        i+=1
        k+=1

    while j<len(uA):
        A[k] = uA[j]
        j += 1
        k += 1

    return A