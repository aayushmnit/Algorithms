def MergeSort(x):
    """
    Implementation of merge sort algorithm nlog(n) complexity
    x : list
    """
    # List of size 1 or empty list
    if len(x) <= 1:
        return x
        # Divide

    ## Find the middle point
    n = int(len(x) / 2)

    y = x[:n]
    z = x[n:]

    # Recursion you beauty
    y = MergeSort(y)
    z = MergeSort(z)

    # Merge logic
    finalOutput = []

    ## Caculating length of arrays to track upper bound
    yLen = len(y)
    zLen = len(z)

    ## Initiate pointers
    i, j = 0, 0

    for k in range(len(x)):
        # Check if first list is completely in final output
        if (i + 1) > yLen:
            return finalOutput + z[j:]
        # Check if second list is completely in final output
        if (j + 1) > zLen:
            return finalOutput + y[i:]

        ## Sort two numbers, if tie take from first array
        if y[i] <= z[j]:
            finalOutput.append(y[i])
            i += 1
        else:
            finalOutput.append(z[j])
            j += 1

    return finalOutput

