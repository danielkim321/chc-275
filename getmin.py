def getMin(userList):
    minValue = userList[0]
    index = 0

    while index < len(userList):
        if userList[index] < minValue:
            minValue = userList[index]
        index = index + 1

    return minValue


print(getMin([1, 2, 3, 4]))
print(getMin([4, 2, 1, 3]))
