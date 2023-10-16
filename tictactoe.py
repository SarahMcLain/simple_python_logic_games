import random
#intro statement
print("Ready to play tic-tac-toe?")
#functiont that creates the tictactoe board
def printBoard(board): 
    print(board[0]+ "|" + board[1] + "|" + board[2])
    print("-----")
    print(board[3]+ "|" + board[4] + "|" + board[5])
    print("-----")
    print(board[6]+ "|" + board[7] + "|" + board[8])
    return board

#function to take player input
def playerInput(board):
    userinput = int(input("Enter a number 1-9   "))
    if userinput >= 1 and userinput <= 9 and board[userinput-1] == "-":
        board[userinput-1] = currentPlayer
    else:
        print("Oops spot not available!")

#function to check for win horizontal
def checkHorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True
#function to check win columns  
def checkColumn(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True

#function to check win diaganol 
def checkDiag(board):
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True
    
#function to check tie
def checkTie(board):
    global gameRunning
    if "-" not in board:
        print(board)
        print("Tie!")
        gameRunning = False

#function that checks win for all three win scenarios
def checkWin():
    if checkDiag(board) or checkHorizontal(board) or checkColumn(board):
        print(f"The winner is {winner}")
        global gameRunning
        gameRunning = False

#switch player if none of the win condtions are true
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"

#function to add computer player
def computer(board):
    while currentPlayer == "O":
        position = random.randint(0,8)
        if board[position] == "-":
            board[position] = "O"
            switchPlayer()

#create a function of the game playing that calls all the functions to make the game work
def playGame():
    while gameRunning:
        printBoard(board)
        playerInput(board)
        checkWin()
        checkTie(board)
        switchPlayer()
        computer(board)
        # checkWin()
        checkTie(board)

#start the game
while True:
        #print a gameboard
    board = ["-", "-", "-",
            "-", "-", "-",
            "-", "-", "-"]
    #set current player to X
    currentPlayer = "X"
    #initialize variables to keep track of game stats
    winner = None
    gameRunning = True

    #call function to play the game
    playGame()

    #ask player if they want to play again when game is finished if answer not yes exit game
    answer = str(input("Would you like to play again? ('yes/no')"))
    if answer.lower() != 'yes':
        break 