import random

r = "rock"
p = "paper"
s = "scissor"
var2 = r, p, s

def replay():
    x = input("Play again: \n Y\\N?  ").lower()
    if x == "yes" or x == "y" or x == "ye":
        game()

    elif x == "no" or x == "n" or x == "ne":
        print("bye!")
        exit()
def game():
    v = input("Chose rock, paper or scissor: ").lower()

    ran = random.choice(var2)
    print(f"{v} vs {ran}")

    if (v == "scissor" and ran == "rock") or (v == "paper" and ran == "scissor") or (v == "rock" and ran == "paper"):
        print("You lost!")
    elif (ran == "scissor" and v == "rock") or (ran == "paper" and v == "scissor") or (ran == "rock" and v == "paper"):
        print("You won!")
    elif(ran == "scissor" and v == "scissor") or (ran == "paper" and v == "paper") or (ran == "rock" and v == "rock"):
        print("It's a draw!")
    else:
        print("Incorrect input!")

    #replay()


#game()
