#Rock,paper and Scissors
# Rock can beat Scissors , Scissors can beat paper and Paper can beat
# Rockimport pandas as p
import random as rnd
game_validator = {'parent': ['rock', 'paper', 'scissors'], 'child': [
    'scissors', 'rock', 'paper']}


while True:

    print("\nRock,paper and Scissors\n" + "*" *
          (len("Rock,paper and Scissors")))

# Deciding the Opponent
# *********************

    while True:
        flag_opponent = str.lower(input("wanna play with computer(y/n) : "))

        if flag_opponent == 'n' or flag_opponent == 'y':
            break
        else:
            print("\nWrong input, you have to enter either y or n \n")

# PLayer1 input
# *********************

    if flag_opponent == 'y':
        player_name = 'Computer'
        print("\nYour opponent is computer and you are the player2\n" + "*" *
              (len("Your opponent is computer and you are the player2")))
        player1 = game_validator['parent'][rnd.randint(0, 2)]
    else:
        player_name = 'Player1'
        print("\nyou are on two player mode\n" + "*" *
              (len("Your opponent is computer and you are the player2")))
        player1 = str.lower(
            input("Player1 Please choose \"rock or paper or scissors\" , your move: "))

# PLayer2 input
# *********************

    player2 = str.lower(
        input("Player2 Please choose \"rock or paper or scissors\" , your move: "))

# Decision maker
# *********************
    print(f"\nSHOOT!! {player_name} vs Player2.....\n")
    if game_validator['parent'].__contains__(
            player1) and game_validator['parent'].__contains__(player2):

        if game_validator['parent'].index(
                player1) == game_validator['child'].index(player2):
            print(f"{player_name} wins....CONGRATZZ")
        elif game_validator['parent'].index(player2) == game_validator['child'].index(player1):
            print("Player2 wins....CONGRATZZ")
        else:
            print("Its a Draw!!")
    else:
        print("Wrong input , you have to enter either of below three options\n 1. rock \n 2. paper \n 3. scissors \n")

# Game controller
# *********************

    while True:
        flag = str.lower(input("wanna play again (y/n) : "))

        if flag == 'n' or flag == 'y':
            break
        else:
            print("\nWrong input, you have to enter either y or n \n")
    if flag == 'n':
        break
