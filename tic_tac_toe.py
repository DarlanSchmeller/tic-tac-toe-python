import os
import random
os.system('clear')

game_board = ['1','2','3','4','5','6','7','8','9']
player_turn = random.randint(1,2)
game_status = True

def display_board(game_board):
    print('')
    print('-------------')
    print(f'| {game_board[0]} | {game_board[1]} | {game_board[2]} |')
    print('|---|---|---|')
    print(f'| {game_board[3]} | {game_board[4]} | {game_board[5]} |')
    print('|---|---|---|')
    print(f'| {game_board[6]} | {game_board[7]} | {game_board[8]} |')
    print('-------------')
    print('')

def player_recognition():
    player_choice = 'Wrong'
    accepted_choice = ['X','O']
    player1 = None
    player2 = None

    while player_choice not in accepted_choice:
        choice = input(f'Player {player_turn}: Do you want to be X or O? ').upper()

        if choice in accepted_choice:
            player_choice = choice
        else:
            print("Invalid option, Please try again")

    if player_choice == 'X':
        player1 = 'X'
        player2 = 'O'
    else:
        player1 = 'O'
        player2 = 'X'

    return player1, player2

def player_position_choice(game_board, player, player_turn):
    accepted_position_range = ['1','2','3','4','5','6','7','8','9', '10']
    position_choice = 'wrong'

    while position_choice.isdigit() == False:
        option = input(f'Player {player_turn}: Pick a position from 1 to 9 (1-9):  ')

        if option.isdigit() and option in accepted_position_range:
            if game_board[int(option)-1] not in ['X', 'O']:
                position_choice = option
            else:
                print('This position has already been chosen, pick another')
        else:
            print('Please enter a number and make sure it is in the correct range.')
    
    game_board[int(position_choice)-1] = player.upper()
    return game_board

def verify_win(game_board):
    results_string = ''.join(game_board)

    horizontal_line_1 = results_string[0:3]
    horizontal_line_2 = results_string[3:6]
    horizontal_line_3 = results_string[7:10]

    vertical_line_1 = results_string[0] + results_string[3] + results_string[6]
    vertical_line_2 = results_string[1] + results_string[4] + results_string[7]
    vertical_line_3 = results_string[2] + results_string[5] + results_string[8]

    diagonal_line1 = results_string[0] + results_string[4] + results_string[8]
    diagonal_line2 = results_string[2] + results_string[4] + results_string[6]


    # Verify each horizontal line for a Win
    if 'XXX' in horizontal_line_1 or 'OOO' in horizontal_line_1:
        return True
    elif 'XXX' in horizontal_line_2 or 'OOO' in horizontal_line_2:
        return True
    elif 'XXX' in horizontal_line_3 or 'OOO' in horizontal_line_3:
        return True

    # Verify each horizontal line for a Win
    if 'XXX' in vertical_line_1 or 'OOO' in vertical_line_1:
        return True
    elif 'XXX' in vertical_line_2 or 'OOO' in vertical_line_2:
        return True
    elif 'XXX' in vertical_line_3 or 'OOO' in vertical_line_3:
        return True
    
    # Verify each diagonal line for a Win
    if 'XXX' in diagonal_line1 or 'OOO' in diagonal_line1:
        return True
    elif 'XXX' in diagonal_line2 or 'OOO' in diagonal_line2:
        return True


    for item in game_board:
        if item not in ['X', 'O']: # Verify if each field was filled            
            # If it finds an Empty field it returns False so the game can continue
            return False
    
    # If it run all verifications and all positions are filled return Tie
    return 'Tie'
            
def game_on(player_turn):
    while game_status:
        if player_turn == 1:
            player_position_choice(game_board, player1, player_turn)
        elif player_turn == 2:
            player_position_choice(game_board, player2, player_turn)
        os.system('clear')
        display_board(game_board)

        if verify_win(game_board) == 'Tie':
            print('Game has tied, no winners.')
            return False
        elif verify_win(game_board) == True:
            print(f'Game Over, Victory for Player {player_turn}!')
            print('')
            return False

        else:
            if player_turn == 1:
                player_turn = 2
            else:
                player_turn = 1


print('Welcome to Tic Tac Toe!')
display_board(game_board)
player1, player2 = player_recognition()
game_on(player_turn)