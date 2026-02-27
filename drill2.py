def makeLists():
    nums = []
    running = True
    while running: 
        numbers = input("what is your number")
        if numbers == "quit":
            running = False 
        numbers = int(numbers)
        nums.append(numbers)
        print(nums)
    return nums
            
list1 = makeLists()
print(list)
list2 = makeLists()
print(list2)
 