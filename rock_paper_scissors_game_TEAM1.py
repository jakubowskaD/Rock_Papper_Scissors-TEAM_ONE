import random


def computer_choice():
    choices = ['rock', 'paper', 'scissor']
    return random.choice(choices)

scoretable = [0,0]
def score_computer():
    scoretable[0] = scoretable[0] + 1
def score_player():
    scoretable[1] = scoretable[1] + 1

def run_game():
    print("")
    print("Game begins")
    
    computer = computer_choice()
    player = input("Choose 1=rock, 2=paper, 3=scissor: ")
    if (player != "1" and player != "2" and player!="3"):
        print("Invalid choice")
        return
    
    test = player + computer[0]
    player_winning_condition = ['1s', '2r', '3p']
    player_draw_condition = ['1r', '2p', '3s']

    print("Computer picked:", computer)
    if (test in player_winning_condition):
        print("You won!")
        score_player()
    elif (test in player_draw_condition):
        print("Draw!")
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
        play_again = input("Play Again? [Y/n]: ")
        if (play_again == "" or play_again == "Y" or play_again == "y"):
            break
        elif (play_again == "n" or play_again == "N"):
            game_finish()
        else:
            print("Wrong choice, try again")
    







