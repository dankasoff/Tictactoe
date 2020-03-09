def display_board(board):
    print(board[7]+'|'+board[8]+'|'+board[9])
    print('-----')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-----')
    print(board[1]+'|'+board[2]+'|'+board[3])

test_board = [' ']*10

def player_input():
    marker=''
    while marker != 'X' and marker != 'O':
        marker = input('Player 1: choose X or O: ').upper()
    if marker == 'X':
        return('X','O')
    else:
        return('O','X')


def place_marker(board,marker,position):
    board[position] = marker

def check_win(board,mark):
    return((board[1]+board[2]+board[3]==mark+mark+mark) or #rows
    (board[4]+board[5]+board[6]==mark+mark+mark) or
    (board[7]+board[8]+board[9]==mark+mark+mark) or
    (board[1]+board[4]+board[7]==mark+mark+mark) or #columns
    (board[2]+board[5]+board[8]==mark+mark+mark) or
    (board[3]+board[6]+board[9]==mark+mark+mark) or
    (board[1]+board[5]+board[9]==mark+mark+mark) or #diagonals
    (board[3]+board[5]+board[7]==mark+mark+mark))

import random

def choose_first():
    FirstChoice = random.randint(1,2)
    return('Player'+str(FirstChoice)+' goes first')

def space_check(board,position): #step6
    if board[position] == ' ':
        return True#('Space is open')
    else:
        return False #('Space is full')

def full_board_check(board): #step7
#    for i in range(1,10):
#        if space_check(board,i) == 'Space is open':
#            return False
#    return True
    if board[1] != ' ' and board[2] != ' ' and board[3] != ' ' and board[4] != ' ' and board[5] != ' ' and board[6] != ' ' and board[7] != ' ' and board[8] != ' ' and board[9] != ' ':
        return True #('Board is full')
    else:
        return False #('Board is not full')

def player_choice(board): #step8
    position = 0
    while position not in range(1,10) or not space_check(board,position):
        position = int(input('Choose a position: (1-9)'))
    return position


def replay(): #step9
    choice = input('play again? Yes or No?')
    return choice
    #return choice == 'Yes'


print('welcome to tic tac toe')
while True:
    the_board = [' ']*10
    player1_marker,player2_marker = player_input()
    turn = choose_first()
    print(turn)
    play_game = input('ready to play? yes or no?')
    if play_game == 'yes':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player1 goes first':
            display_board(the_board) #show board
            position = player_choice(the_board) #choose position
            place_marker(the_board,player1_marker,position) #place marker in position
            if check_win(the_board,player1_marker):#check if they won
                display_board(the_board)
                print('player 1 has won')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('tie game')
                    break
                else:
                    turn = 'Player2 goes first'
            #in case of tie
        else:
            display_board(the_board)  # show board
            position = player_choice(the_board)  # choose position
            place_marker(the_board, player2_marker, position)  # place marker in position
            if check_win(the_board, player2_marker):  # check if they won
                display_board(the_board)
                print('player 2 has won')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('tie game')
                    break
                else:
                    turn = 'Player1 goes first'


    if not replay():
        break
