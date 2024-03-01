import quiz
import Random

def select():
    try:
        Game = int(input("Which game would you like to play:\n "
                     "1) Rock,Paper, Scissor\n "
                     "2) Quiz\n 3) Exit\n  "))

        if Game == 1:
                Random.game()
                replay()
        elif Game == 2:
                quiz.quiz()
                replay()
        elif Game == 3:
                print("see you again. Bye :)")
                return
    except Exception as e:
        print(e)
        print("\nPlease type in a number only to chose the desired option: \n")
        select()

def replay():
    x = input("Play again?: \n Y\\N  ").lower()
    if x == "yes" or x == "y" or x == "ye":
        select()

    elif x == "no" or x == "n" or x == "ne":
        print("Have a nice day. Bye !")
        return
select()