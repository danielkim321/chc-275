x  = input("what is the power level of the first monster? ")
y = input("What is the power level of the second monster")
x = int(x)
y = int(y)
if x > y:
    print(f'{x} First monster wins!')
elif y > x:
    print(f'{x} Second monster wins!')
elif x == y:
    print("its a tie!")

          