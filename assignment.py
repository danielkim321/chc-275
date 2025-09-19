print("Welcome to Hailstone Simulator! ")
x  = input("please enter a height for the hailstone to start at: ")
var = False
while var == False:
    x = int(x)
    if x % 2 ==0:
        x /=2
        print(f"{x}")
        if x == 1:
         var = True
    else: 
        x *=3
        x +=1
        print(f"{x}")
        if x == 1:
            var = True 







