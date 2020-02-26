import random

rounds = 0  # rounds played
wins = 0    # wins earned
draws = 0   # draw situations


def ComputerChoice():  # Generate computer's choice
    computer = random.randint(0, 2)
    if computer == 0:
        print("Computer chooses: Rock")
        return computer
    elif computer == 1:
        print("Computer chooses: Paper")
        return computer
    else:
        print("Computer chooses: Scissors")
        return computer


def CheckWinner(player, computer):  # Check winner of the round
    global rounds, wins, draws
    if player == "Rock":
        if computer == 0:
            print("\nDraw!")
            draws += 1
            rounds += 1

        elif computer == 1:
            print("\nYou lost!")
            rounds += 1

        else:
            print("\nYou win!")
            wins += 1
            rounds += 1

    elif player == "Paper":
        if computer == 0:
            print("\nYou win!")
            wins += 1
            rounds += 1

        elif computer == 1:
            print("\nDraw!")
            draws += 1
            rounds += 1

        else:
            print("\nYou lost!")
            rounds += 1

    elif player == "Scissors":
        if computer == 0:
            print("\nYou lost!")
            rounds += 1

        elif computer == 1:
            print("\nYou win!")
            wins += 1
            rounds += 1
        else:
            print("\nDraw!")
            draws += 1
            rounds += 1


# Game running in loop until Quit
while True:

    # Ask player's choice
    player = input("\nRock, Paper or Scissors? (type Quit to end game): ")

    if player not in ("Rock", "Paper", "Scissors", "Quit"):  # Warning if invalid input
        print("\nPlease choose Rock, Paper or Scissors to play, or Quit to end the game!")

    elif player == "Quit":  # Quit game
        print("\nYou played", rounds, "rounds of which you won",
              wins, "and got a draw", draws, "times.")
        break

    else:
        print("\nYou choose: ", player)

        computer = ComputerChoice()

        CheckWinner(player, computer)
