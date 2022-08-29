from statistics import mean, median

def listAverage(listOfLists):
    result = []

    #Check if Lists have the same length
    listLength, listLen = [], len(listOfLists[0])
    [listLength.append(len(li)) for li in listOfLists]
    if not mean(listLength) == listLen: return None

    #Create Average (Median) List of ListOfLists
    newList = []
    for i in range(0, listLen):
        listIndex = []
        for item in listOfLists:
            listIndex.append(item[i])
        newList.append(round(median(listIndex), 3))        
    return newList