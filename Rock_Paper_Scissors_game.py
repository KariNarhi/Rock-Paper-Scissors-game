import random

rounds = 0
wins = 0
draws = 0


def ComputerChoice():
    computer = random.randint(0, 2)
    if computer == 0:
        print("computer chooses: Rock")
        return computer
    elif computer == 1:
        print("computer chooses: Paper")
        return computer
    else:
        print("computer chooses: Scissors")
        return computer


def CheckWinner(player, computer):
    global rounds, wins, draws
    if player == "Rock":
        if computer == 0:
            print("Draw!")
            draws += 1
            rounds += 1

        elif computer == 1:
            print("You lost!")
            rounds += 1

        else:
            print("You win!")
            wins += 1
            rounds += 1

    elif player == "Paper":
        if computer == 0:
            print("You win!")
            wins += 1
            rounds += 1

        elif computer == 1:
            print("Draw!")
            draws += 1
            rounds += 1

        else:
            print("You lost!")
            rounds += 1

    elif player == "Scissors":
        if computer == 0:
            print("You lost!")
            rounds += 1

        elif computer == 1:
            print("You win!")
            wins += 1
            rounds += 1
        else:
            print("Draw!")
            draws += 1
            rounds += 1


while True:

    player = input("\nRock, Paper or Scissors? (type Quit to end game): ")

    if player not in ("Rock", "Paper", "Scissors", "Quit"):
        print("\nPlease choose Rock, Paper or Scissors to play, or Quit to end the game!")

    elif player == "Quit":
        print("\nYou played", rounds, "rounds of which you won",
              wins, "and got a draw", draws, "times.")
        break

    else:
        print("You choose: ", player)

        computer = ComputerChoice()

        CheckWinner(player, computer)
