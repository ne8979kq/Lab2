def CreateMenu(listOfChoices,menuTitle):
    bigStr = menuTitle + '\n'
    count = 1
    for choice in listOfChoices:
        littleStr = str(count) + '. ' + choice +'\n'
        count += 1
        bigStr += littleStr
    return bigStr
