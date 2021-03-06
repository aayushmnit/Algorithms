def AddZeros(x, n, left=True):
    """
    x is a string
    n is number of zeros to be added
    left true meaning leading zeros, false meaning lagging zeroes
    """
    if left:
        return str(0) * n + x
    else:
        return x + str(0) * n


def KaratsubaMultiplier(x, y):
    ## Convert x and y to string for easier string manipulation
    x = str(x)
    y = str(y)

    ## Determining N for the split
    if len(x) >= len(y):
        n = len(x)
    else:
        n = len(y)

    ## Base case
    if n == 1:
        return int(x) * int(y)

    ## Making n an even number
    if n % 2 != 0:
        n += 1

    ## Adding leading zeros to make even lengths
    x = AddZeros(x, n - len(x))
    y = AddZeros(y, n - len(y))

    n_half = int(n / 2)
    
    ## Finding a, b, c, d
    a = x[:n_half]
    b = x[n_half:]
    c = y[:n_half]
    d = y[n_half:]

    ## Recursion you beauty
    ac = KaratsubaMultiplier(a, c)
    bd = KaratsubaMultiplier(b, d)
    abcd = KaratsubaMultiplier(int(a) + int(b), int(c) + int(d))
    sub = abcd - ac - bd

    return int(AddZeros(str(ac), n, False)) + bd + int(AddZeros(str(sub), n_half, False))
