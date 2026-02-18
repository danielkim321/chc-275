def getMedian(userList):
    x = len(userList)

    
    if x % 2 == 1:
        return userList[x // 2]
    else:
        return (userList[x // 2 - 1] + userList[x // 2]) / 2


print(getMedian([1, 2, 3]))
print(getMedian([1, 2, 3, 4]))
