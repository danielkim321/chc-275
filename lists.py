mylist = [1, 2, 3, 4, 5]

print(mylist[0])
sum = mylist[0] + mylist [3]
print(sum)

mylist = [ 5, 10, 15, 20, 25, 30 ,35]
print('printing size')
print(len(mylist))


i = 0
while i <= len(mylist)-1:
    print(mylist[i])
    i = i + 1



print("for loop example")
for x in mylist:
    x = x + 5
print(mylist)

i = 0
while i <= len(mylist)-1:
    mylist[i] = mylist[i] + 5
    print(mylist[i])
    i = i + 1
    
print(mylist)



    