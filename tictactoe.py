import os

# Using py dictionary as the board
theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def printBoard(board):
    print("")
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
    print("")

def checkTie(board):
    if " " not in list(board.values()):
        return True

def checkWin(board):
    # Horizontal
    if board['top-L'] == board['top-M'] == board['top-R'] != ' ':
        return True
    if board['mid-L'] == board['mid-M'] == board['mid-R'] != ' ': 
        return True
    if board['low-L'] == board['low-M'] == board['low-R'] != ' ':
        return True
    # Vertical
    if board['top-L'] == board['mid-L'] == board['low-L'] != ' ':
        return True
    if board['top-M'] == board['mid-M'] == board['low-M'] != ' ':
        return True
    if board['top-R'] == board['mid-R'] == board['low-R'] != ' ':
        return True
    # Horizontal
    if board['top-L'] == board['mid-M'] == board['low-R'] != ' ':
        return True
    if board['top-R'] == board['mid-M'] == board['low-L'] != ' ':
        return True
    
    # Check Tie
    if checkTie(board):
        return False

message = "Welcome to Tic-Tac-Toe!"     # On game start!
list_of_move = list(theBoard.keys())
turn = 'X'

for i in range(9):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(message)
    print(f"List of moves: {list_of_move}")
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    move = input()

    # Checking for valid move
    if move not in list_of_move:
        message = "Please enter a valid move!"
        continue 
    
    # Checking whether the spot is taken
    if theBoard[move] == ' ':
        theBoard[move] = turn
        message = "Tic-Tac-Toe"
    else:
        message = "The spot is taken. Choose another one!"
        continue

    # Check for win
    if checkWin(theBoard):
        os.system('cls' if os.name == 'nt' else 'clear')
        printBoard(theBoard)
        print(f"{turn} Win!")
        break
    elif checkWin(theBoard) == False:
        os.system('cls' if os.name == 'nt' else 'clear')
        printBoard(theBoard)
        print("Tie!")
        break

    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'