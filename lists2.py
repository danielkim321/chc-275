mylist = [1, 2, 3, 4, 5]

for i in range(len(mylist)):
        mylist[i] = mylist[i] + 5
    
print(mylist)

mylist.append(15) 
print(mylist)
mylist.pop(0)
print(mylist)
mylist.remove(9)
print(mylist)