def DiagDiff(theList):
    ltorSum, rtolSum = 0,0
    howlong = len(theList)
    i = 0
    j = 0
    while(i < howlong):
        ltorSum += theList[i][j]
        i += 1
        j += 1

    i = 0
    j = howlong - 1
    while(i < howlong):
        rtolSum += theList[i][j]
        i += 1
        j -= 1
    return abs(ltorSum - rtolSum)
print(DiagDiff(theList =[[11, 2, 4],[4, 5, 6],[10, 8, -12]]))
