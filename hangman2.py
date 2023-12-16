Q_Hint='Animals'
Q_Word=['l','i','o','n']
answer=[]
turns=5
User_Name=input("enter your name : ")
print("Hello "+ User_Name + " Let's start the game : ")
print("The clue is : " + Q_Hint)
print("Start Guessing the Word : ")
while turns != 0:
    for i in Q_Word:
        if i in answer:
            print(i,end='')
        else:
            print('_',end='')
    if answer==Q_Word:
        print()
        print('you won')
        break
    alpha=input(" Guess a Letter : ")
    answer.append(alpha)
    if alpha not in Q_Word:
        turns-=1
        print ("Wrong")
        print ("You have", + turns, 'more chances' )
    if turns==0:
        print('You loose')



