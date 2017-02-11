'''Find the minimum length subarray which when sorted, sorts the entire array.'''


def minLength(A):
    if len(A) == 0 or len(A) == 1:
        return 0

    start = None
    for i in range(1,len(A)):
        if A[i-1] > A[i]:
            start = i-1
            break

    end = None
    for i in range(len(A)-1, -1, -1):
        if A[i-1] > A[i]:
            end = len(A) - i + 1
            break

    minN = min(A[start:end+1])
    maxN = max(A[start:end+1])

    minPos = None
    for i in range(0, len(A)):
        if minN < A[i]:
            minPos = i
            break

    maxPos = None
    for i in range(len(A)-1, -1, -1):
        if maxN > A[i]:
            maxPos = i
            break

    return maxPos - minPos