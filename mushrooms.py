small = []
medium = []
large = []

check = False
while check == False:
    option = input("Enter mushroom size or type 'stop': ")

    if option == "stop":
        check = True
        print("stopping...")
    
    elif option >= "0" and option <= "9999":  
        option = int(option)

        if option < 100:
            small.append(option)
        elif option >= 100 and option < 200:
            medium.append(option)
        else:
            large.append(option)
    else:
        print("Please enter a number.")

print("Small mushrooms:", small)
print("Medium mushrooms:", medium)
print("Large mushrooms:", large)
