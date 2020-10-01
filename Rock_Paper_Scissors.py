from random import randint


t = ["Rock", "Paper", "Scissors"]

computer = t[randint(0,2)]
computercount, playercount = 0, 0

player = False
while player == False and computercount <3 and playercount < 3:

    player = input("Rock, Paper, Scissors?")
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
            computercount += 1
        else:
            print("You win!", player, "smashes", computer)
            playercount += 1
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
            computercount += 1
        else:
            print("You win!", player, "covers", computer)
            playercount += 1
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
            computercount += 1 
        else:
            print("You win!", player, "cut", computer)
            playercount += 1 
    else:
        print("That's not a valid play. Check your spelling!")

    player = False
    computer = t[randint(0,2)]