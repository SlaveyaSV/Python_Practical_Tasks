import random


def computer_choice():
    computer_number = random.randint(1, 3)
    computer_move = ""

    if computer_number == 1:
        computer_move = "Rock"
    elif computer_number == 2:
        computer_move = "Paper"
    elif computer_number == 3:
        computer_move = "Scissors"

    return computer_move


def player_choice(player_input):
    player_move = ""

    if player_input == "r":
        player_move = "Rock"
    elif player_input == "p":
        player_move = "Paper"
    elif player_input == "s":
        player_move = "Scissors"
    else:
        player_move = "Invalid"

    return player_move


def current_winner(player_move, computer_move, player_score, computer_score):
    if (player_move == "Rock" and computer_move == "Scissors") or \
       (player_move == "Scissors" and computer_move == "Paper") or \
       (player_move == "Paper" and computer_move == "Rock"):
        print_green("You win!")
        player_score += 1
    elif computer_move == player_move:
        print_yellow("Draw!")
    else:
        print_red("You lose!")
        computer_score += 1
    return player_score, computer_score


def game_winner(player_score, computer_score):
    if player_score > computer_score:
        print_green(f"\nYou won the game with final result {player_score}:{computer_score}")
    elif player_score < computer_score:
        print_red(f"\nYou lost the game with final result {player_score}:{computer_score}")
    else:
        print_yellow(f"\nThe game is draw with final result {player_score}:{computer_score}")


def print_blue(skk): print("\033[34m {}\033[00m".format(skk))
def print_cyan(skk): print("\033[36m {}\033[00m".format(skk))
def print_red(skk): print("\033[91m {}\033[00m".format(skk))
def print_green(skk): print("\033[92m {}\033[00m".format(skk))
def print_yellow(skk): print("\033[93m {}\033[00m".format(skk))


computer_total_score = 0
player_total_score = 0

while True:
    input_player = input("\nEnter your choice: r, p or s for Rock, Paper or Scissors: ")

    if player_choice(input_player) == "Invalid":
        print("Invalid input! Please try again...")
        continue
    else:
        choice_player = player_choice(input_player)
        choice_computer = computer_choice()
        print_blue(f"Your choice is {choice_player}.")
        print_cyan(f"Computer's random choice is {choice_computer}.")

    player_total_score, computer_total_score = \
        current_winner(choice_player, choice_computer, player_total_score, computer_total_score)

    print(f"Your score: {player_total_score}")
    print(f"Computer score: {computer_total_score}")

    print("\nWould you like to play again?")
    another_game = input("Choose y for Yes or n for No ")

    while "n" != another_game != "y":
        print("\nInvalid choice! Please try again...")
        another_game = input("Choose y for Yes or n for No ")

    if another_game == "n":
        game_winner(player_total_score, computer_total_score)
        print("Thank you for playing! Goodbye!")
        break
    elif another_game == "y":
        continue
