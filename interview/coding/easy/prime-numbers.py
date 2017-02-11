'''Find all of the prime numbers less than n.'''


def primeNumbers(n):
    res = []
    for i in range(2, n):
        if prime(i):
            res.append(i)

    return res


def prime(n):
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False

    return True