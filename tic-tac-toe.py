board=["-","-","-",
       "-","-","-",
       "-","-","-"]

currentPlayer="X"
gameRunning=True
winner = None

def printBoard(board):
    for i in range(1,10):
        print(f"{board[i-1]} ",end="")
        if i%3==0:
            print("\n")


def playerMove(board):
    move=int(input("Enter number from 1-9: "))
    if 1<=move<=9 and board[move-1]=="-":
        board[move-1]=currentPlayer
    else:
        print("Please enter a valid option")
        playerMove(board)
    
def winByRow(board):
    global winner
    
    for i in range(0,9,3):
        if board[i]==board[i+1]==board[i+2] and board[i]!="-":
            winner=board[i]
            return True
        
def winByCol(board):
    global winner
    for i in range(0,3):
        if board[i]==board[i+3]==board[i+6] and board[i]!="-":
            winner=board[i]
            return True

def winBydia(board):
    global winner
    global currentPlayer
    if (board[0] == board[4] == board[8] and board[0] != "-"):
        winner = board[0]
        return True
    elif (board[2] == board[4] == board[6] and board[2]!="-"):
        winner = board[2]
        return True
    
def checkTie(board):
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("The match has ended in a tie")
        gameRunning=False


def switchPlayer():
    global currentPlayer
    if currentPlayer=="X":
        currentPlayer="O"
    else:
        currentPlayer="X"

def checkWin(board):
    global gameRunning
    if winByRow(board) or winByCol(board) or winBydia(board):
        printBoard(board)
        print(f"{winner} won")
        
        gameRunning=False


while (gameRunning):
    printBoard(board)
    if winner!=None:
        break
    playerMove(board)
    switchPlayer()
    checkWin(board)
    checkTie(board)
