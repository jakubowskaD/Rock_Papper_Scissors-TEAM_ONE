import random


def computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

scoretable = [0,0]

def player_choice(player):
    if player == "1":
        player_choice = "rock"
    elif player == "2":
        player_choice = "paper"
    else:
        player_choice = "scissors"
    return player_choice

scoretable = [0,0]
def score_computer():
    scoretable[0] = scoretable[0] + 1
def score_player():
    scoretable[1] = scoretable[1] + 1

def run_game():
    print("\nGame begins") 
    
    computer = computer_choice()
    player = input("Choose 1 = rock, 2 = paper, 3 = scissors: ")
    if (player != "1" and player != "2" and player!="3"):
        print("Invalid choice")
        return
    
    test = player + computer[0]
    player_winning_condition = ['1s', '2r', '3p']
    player_draw_condition = ['1r', '2p', '3s']

    print("You picked: ", player_choice(player))
    print("Computer picked:", computer)
    if (test in player_winning_condition):
        print("You won!")
        score_player()
    elif (test in player_draw_condition):
        print("It's a draw!")
    else:
        print("You lost!")
        score_computer()
    print("")
    score_display()
    

def score_display():
    print("")
    print("--------------------------------")
    print("Score table")
    print("Computer:", scoretable[0])
    print("Player:", scoretable[1])

    

def game_finish():
    score_display()
    input("Press enter to exit")
    quit()


while (True):
    run_game()

    while (True):
        play_again = input("Play Again? [Y/n]: ").lower()
        if play_again == "" or play_again == "y":
            break
        elif play_again == "n":
            game_finish()
        else:
            print("Wrong choice, try again")
    







