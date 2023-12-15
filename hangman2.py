import random
print("welcome to handman game")
print("guess the 3 numbers from 1 to 10 ")
list1=[1,2,3,4,5,6,7,8,9]
display1=random.choice(list1)
list2=[1,2,3,4,5,6,7,8,9]
display2=random.choice(list2)
list3=[1,2,3,4,5,6,7,8,9]
display3=random.choice(list3)
list4=[1,2,3,4,5,6,7,8,9]
display4=random.choice(list4)
list5=[1,2,3,4,5,6,7,8,9]
display5=random.choice(list5)
list6=[1,2,3,4,5,6,7,8,9]
display6=random.choice(list6)

op1=int(input("enter your first number:-"))
if op1==display1:
    print("ur first number is correct")
else:
    print("ur first number is wrong")
    print("o")
op2=int(input("enter your second number:-"))
if op2==display2:
    print("ur second number is correct")
else:
    print("ur second number is wrong")
    print("o")
    print("|")
op3=int(input("enter your third number:-"))
if op3==display3:
    print("ur third number is correct")
else:
    print("ur third number is wrong")
    print(" o")
    print("\|")
op4=int(input("enter your fourth number:-"))
if op4==display4:
    print("ur fourth number is correct")
else:
    print("ur fourth number is wrong")
    print(" o")
    print("\|/")
op5=int(input("enter your fifth number:-"))
if op5==display5:
    print("ur fifth number is correct")
else:
    print("ur fifth number is wrong")
    print(" o ")
    print("\|/")
    print("/|")
op6=int(input("enter your sixth number:-"))
if op3==display6:
    print("ur sixth number is correct")
else:
    print("ur sixth number is wrong")
    print(" o ")
    print("\|/")
    print("/||")
if op1==display1 and op2==display2 and op3==display3 and op4==display4 and op5==display5 and op6==display6:
        print("****************congratulations********************")
        print("you won the game")
else:
    print("******************sorry*********************")
    print("you loss the game")



