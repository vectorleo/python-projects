theBoard = {
    'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
    'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
    'low-L': ' ', 'low-M': ' ', 'low-R': ' '
    }



def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])



turn = "x"
for i in range(9):
    printBoard(theBoard)
    print(f"turn for {turn}. move to which space?")
    move = input()
    theBoard[move] = turn 
    if turn == "x":
        turn = "o"
    elif turn == "o":
        turn = "x"
    else:
        turn ="X"

printBoard(theBoard)
