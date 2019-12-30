def addZeros(x, n, left=True):
    '''
    x is a string
    n is number of zeros to be added
    left true meaning leading zeros, false meaning lagging zeroes
    '''
    if left:
        return str(0)*n + x
    else:
        return x + str(0)*n

def karatsubaMultiplier(x,y):
    ## Convert x and y to string for easier manipulation
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
    if n%2 != 0:
        n += 1
    
    ## Adding leading zeros to make even lengths
    x = addZeros(x, n-len(x))
    y = addZeros(y, n-len(y))
    
    halfN = int(n/2)
    print(halfN, n)
    ## Finding a, b, c, d
    a = x[:halfN]
    b = x[halfN:]
    c = y[:halfN]
    d = y[halfN:]    

    ## Recursion you beauty
    ac = karatsubaMultiplier(a, c)
    bd = karatsubaMultiplier(b,d)
    abcd = karatsubaMultiplier(int(a)+int(b), int(c)+int(d))

    return (10**n) * ac + bd + (10**halfN)*(abcd - ac- bd)

