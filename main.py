def printBoard(playerX,playerO):
    zero = 'X' if playerX[0] == 1 else ('O' if playerO[0] == 1 else 0)
    one = 'X' if playerX[1] == 1 else ('O' if playerO[1] == 1 else 1)
    two = 'X' if playerX[2] == 1 else ('O' if playerO[2] == 1 else 2)
    three = 'X' if playerX[3] == 1 else ('O' if playerO[3] == 1 else 3)
    four = 'X' if playerX[4] == 1 else ('O' if playerO[4] == 1 else 4)
    five = 'X' if playerX[5] == 1 else ('O' if playerO[5] == 1 else 5)
    six = 'X' if playerX[6] == 1 else ('O' if playerO[6] == 1 else 6)
    seven = 'X' if playerX[7] == 1 else ('O' if playerO[7] == 1 else 7)
    eight = 'X' if playerX[8] == 1 else ('O' if playerO[8] == 1 else 8)
    print(f' {zero} | {one} | {two} ')
    print(f'---|---|---')
    print(f' {three} | {four} | {five} ')
    print(f'---|---|---')
    print(f' {six} | {seven} | {eight} ')

def isValid(value):
    if 0<=value<=8:
        if (playerX[value] == 1) or (playerO[value] == 1):
            return False
        return True
    return False

def victory(playerX,playerO):
    wins = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for win in wins:
        if playerX[win[0]] + playerX[win[1]] + playerX[win[2]] == 3:
            print('PlayerX Wins')
            return 1
        elif playerO[win[0]] + playerO[win[1]] + playerO[win[2]] == 3:
            print('PlayerO Wins')
            return 0
    return -1

playerX = [0, 0, 0, 0, 0, 0, 0, 0, 0]
playerO = [0, 0, 0, 0, 0, 0, 0, 0, 0]
turn = 1 #1 for X and 0 for O
total_moves = 0
print("Tic Tac Toe")
while(True):
    printBoard(playerX,playerO)
    if turn == 1:
        print("Player X's Move")
        value = int(input("Please enter a value: "))
        while not(isValid(value)):
            print("Value already Taken / Out of Bound. Please Enter another Value")
            value = int(input("Please enter a value: "))
        playerX[value] = 1
    else:
        print("Player O's Move")
        value = int(input("Please enter a value: "))
        while not(isValid(value)):
            print("Value already Taken / Out of Bound. Please Enter another Value")
            value = int(input("Please enter a value: "))
        playerO[value] = 1
    result = victory(playerX,playerO)
    if result != -1:
        break
    turn = 1 - turn
    total_moves += 1
    if total_moves == 9:
        print("Match Drawn")
        break

#Inspired by CodeWithHarry
