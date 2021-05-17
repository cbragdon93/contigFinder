def getContigs(myList):
    consecutiveResult = []
    myListLength = len(myList)
    thisChunk = []
    # edge case: passed an empty List
    if not myList:
        return None
    elif myListLength == 1:
        return [myList]
    for i in range(1, myListLength):
        thisChunk.append(myList[i-1])
        if(myList[i] - myList[i-1] != 1):
            # need to account for one-length chunks when
            # hitting a stopping point for contig isolation
            if len(thisChunk)>1:
                consecutiveResult.append([thisChunk[0], thisChunk[-1]])
            else:
                consecutiveResult.append(thisChunk)
            thisChunk = []
        # edge case was here. want to detect the end of the
        # list, regardless of contiguity status(i.e. needs to 
        # be its own control block)
        if i == myListLength-1:
            thisChunk.append(myList[i])
            if len(thisChunk)>1:
                consecutiveResult.append([thisChunk[0], thisChunk[-1]])
            else:
                consecutiveResult.append(thisChunk)
    return consecutiveResult
