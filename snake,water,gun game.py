import random

lst = ('r', 'p', 's')
print('game of rock papper scissor')
print('r for rock\n p for papper\n s for scissor ')
chance = 10
no_of_chance = 0
human_point = 0
computer_point = 0
import random

lst = ('r', 'p', 's')
while no_of_chance < chance:
    inp = input("rock,papper,scissor -->")
    ran = random.choice(lst)

    if inp == ran:
        print("draw both choise same so 0 point\n ")
    elif inp == "r" and ran == "p":
        human_point = human_point + 1
        print(f"your guess(inp) and computer guess is(ran)\n")
        print("human got one point \n")
        print(f"computer point is--- {computer_point}--- and human point is--- {human_point}--")
    elif inp == "r" and ran == "s":
        computer_point = computer_point + 1
        print(f"your guess{inp} and computer guess is{ran}\n")
        print("computer got one point \n")
        print(f"computer point is ---{computer_point}--- and human point is -----{human_point}--")
    elif inp == "p" and ran == "r":
        computer_point = computer_point + 1
        print(f"your guess{inp} and computer guess is{ran}\n")
        print("computer got one point \n")
        print(f"computer point is ---{computer_point}--- and human point is-- {human_point}--")
    elif inp == "p" and ran == "s":
        human_point = human_point + 1
        print(f"your guess{inp} and computer guess is{ran}\n")
        print("human got one point \n")
        print(f"computer point is-- {computer_point}-- and human point is ---{human_point}--")
    elif inp == "s" and ran == "r":
        human_point = human_point + 1
        print(f"your guess{inp} and computer guess is{ran}\n")
        print("human got one point \n")
        print(f"computer point is --{computer_point}--- and human point is ----{human_point}--")
    elif inp == "s" and ran == "p":
        computer_point = computer_point + 1
        print(f"your guess{inp} and computer guess is{ran}\n")
        print("computer got one point \n")
        print(f"computer point is--- {computer_point}-- and human point is --{human_point}--")
    else:
        print("wrong input")
    no_of_chance = no_of_chance + 1
    print(f"{chance - no_of_chance}is left out of{chance}")

print("game over")

if computer_point > human_point:
    print('computer win ')
else:
    print('human win ')
print(f"human point is {human_point} and computer point is {computer_point}")