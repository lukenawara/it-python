import random
from banner import banner

def print_welcome_message():
    print("We are going to play rock, paper, scissors.")
    print("The first to win two out of three rounds is the winner.")


def get_player_choice():
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    choice = int(input("What is your choice? "))
    return choice
def print_score (player,cpu):
    print(f"SCORE: Player: {player} Computer: {cpu}")

banner("ROCK, PAPER, SCISSORS" , "Luke")

play_again = True
while play_again:


    print_welcome_message()
    cpu_score = 0
    player_score = 0

    while player_score < 2 and cpu_score < 2:
        print_score(player_score, cpu_score)
        try:
            player_choice = get_player_choice()
        except ValueError:
            print("Not a valid answer. Try again")
            continue
        cpu_choice = random.randint(1,3)
        if player_choice == 1:
            if cpu_choice == 1:
                print ("Tie")
            if cpu_choice == 2:
                print("Lose")
                cpu_score = cpu_score + 1
            if cpu_choice == 3:
                print("Win")
                player_score = player_score + 1

        if player_choice == 2:
            if cpu_choice == 1:
                print ("Tie")
            if cpu_choice == 2:
                print("Lose")
                cpu_score = cpu_score + 1
            if cpu_choice == 3:
                print("Win")
                player_score = player_score + 1

        if player_choice == 3:
            if cpu_choice == 1:
                print ("Tie")
            if cpu_choice == 2:
                print("Lose")
                cpu_score = cpu_score + 1
            if cpu_choice == 3:
                print("Win")
                player_score = player_score + 1
    if player_score >=2:
        print("congratulations! you have defeated the computer! you win this round.")
    elif cpu_score >=2:
        print("Computer wins! You lose.")

    if input("Do you want to keep playing? y/n  ") == "n":
        play_again = False