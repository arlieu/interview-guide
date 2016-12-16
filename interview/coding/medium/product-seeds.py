def productSeeds(n):
    for i in range(n):
        if product(i) == n:     #  final result of product will be n if it is a product seed
            print(i, end = " ")


def product(n):
    res = n
    while n != 0:
        res *= n % 10       #  computes potential seed
        n //= 10            #  next significant digit
    return res