def MergeSortWithInversion(x):
    """
    Implementation of merge sort algorithm nlog(n) complexity
    x : list
    """
    # List of size 1 or empty list
    if len(x) <= 1:
        return x, 0
        # Divide

    ## Find the middle point
    n = int(len(x) / 2)

    y = x[:n]
    z = x[n:]

    # Recursion you beauty
    y, leftInvCount = MergeSortWithInversion(y)
    z, rightInvCount = MergeSortWithInversion(z)

    # Merge logic
    finalOutput = []

    ## Counting number of left and right inversions
    invCount = leftInvCount + rightInvCount

    ## Caculating length of arrays to track upper bound
    yLen = len(y)
    zLen = len(z)

    ## Initiate pointers
    i, j = 0, 0

    for k in range(len(x)):
        # Check if first list is completely in final output
        if (i + 1) > yLen:
            return finalOutput + z[j:], invCount
        # Check if second list is completely in final output
        if (j + 1) > zLen:
            return finalOutput + y[i:], invCount

        ## Sort two numbers, if tie take from first array
        if y[i] <= z[j]:
            finalOutput.append(y[i])
            i += 1
        else:
            finalOutput.append(z[j])
            j += 1

            # Counting number of split inversions 
            # By adding remaining length of y whenever an element of z array is added to the sorted list before elements of y
            invCount += yLen - i

    return finalOutput, invCount

