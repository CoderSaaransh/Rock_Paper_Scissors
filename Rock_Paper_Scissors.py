import random

User_Wins = 0
Comp_Wins = 0
Tie = 0

options = ['rock','paper','scissors']

while True:
    User_Input = input("Type Rock/Paper/Scissors or Q to Quit : ").lower()
    if User_Input == 'q':
        break

    if User_Input not in options:
        continue

    Random_Number = random.randint(0,2)
    Comp_Pick = options[Random_Number]

    print('Computer picked',Comp_Pick)

    if User_Input == 'rock' and Comp_Pick == 'scissors':
        print('You Won!')
        User_Wins +=1

    elif User_Input == 'paper' and Comp_Pick == 'rock':
        print('You Won!')
        User_Wins +=1

    elif User_Input == 'scissors' and Comp_Pick == 'paper':
        print('You Won!')
        User_Wins +=1

    elif User_Input == Comp_Pick :
        print('Tie')
        Tie +=1

    else:
        print('You Lost!')
        Comp_Wins +=1

print("Win ",User_Wins)
print("Lost ", Comp_Wins)
print("Tie ",Tie)


if User_Wins > Comp_Wins :
    print("You Won ")
elif User_Wins == Comp_Wins :
    print("It's a Tie")
else :
    print('You Lost')