"""""
x = 1
while x <= 10:
    #all numbers from 1 to 10
    print(x)
    #x = x + 1 first way 
    x += 1 #second way 
"""

check = False 
while check  == False:
    option = input("Enter your option 1 2 or 3. Type quit to exit: ")
    if option == "1":
        print("option")
    elif option == "2":
        print("option 2")
    elif option == "3":
        print("option 3")
    elif option == "quit":
        check = True 
        
