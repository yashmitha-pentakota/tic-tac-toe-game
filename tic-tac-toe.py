#yashmitha (task-1)
#tictactoe game
import random
game_board=["_" , "_" ,"_",
            "_" ,"_" ,"_",
            "_" ,"_" ,"_" ]
player ="X"
winner = None
gamerunning = True

# game board
def printBoard(game_board):
    print(game_board[0] + " | " + game_board[1] + " | " + game_board[2], "|")
    print("-----------------")
    print(game_board[3] + " | " + game_board[4] + " | " + game_board[5], " | ")
    print("----------------")
    print(game_board[6] + " | " + game_board[7] + " | " + game_board[8], " | ")
    print("-----------------")   
    
#take player input
def playerinput(game_board):
    plyinp=int(input("enter a number "))
    if game_board[plyinp-1]== "_":
        game_board[plyinp-1] = player
        
    else:
        print("Oops!! alredy a player exists")
    
    

#checking for win or tie
def checkhorizontle(game_board):
    global winner 
    if game_board[0] == game_board[1] == game_board[2] and game_board[0]!= "_":
        winner = game_board[0]
        return True
    elif game_board[3] == game_board[4] == game_board[5] and game_board[3]!= "_":
        winner = game_board[3]
        return True
    elif game_board[6] == game_board[7] == game_board[8] and game_board[6]!= "_":
        winner = game_board[6]
        return True
    
def checkrow(game_board):
        global winner 
        if game_board[0] == game_board[3] == game_board[6] and game_board[0]!= "_":
            winner = game_board[0]
            return True
        elif game_board[1] == game_board[4] == game_board[7] and game_board[1]!= "_":
            winner = game_board[1]
            return True
        elif game_board[2] == game_board[5] == game_board[8] and game_board[2]!= "_":
            winner = game_board[2]
            return True

def checkdiag(game_board):
    global winner 
    if game_board[0] == game_board[4] == game_board[8] and game_board[0]!= "_":
            winner = game_board[0]
            return True
    elif game_board[2] == game_board[4] == game_board[6] and game_board[2]!= "_":
            winner = game_board[2]
            return True
        
def checkifwin(game_board):
    global gamerunning
    if checkhorizontle(game_board):
        printBoard(game_board)
        print(f"the winner is {winner}")
        gamerunning=False
    elif checkrow(game_board):
        printBoard(game_board)
        print(f"the winner is {winner}")  
        gamerunning = False
    elif checkdiag(game_board):
        printBoard(game_board)
        print(f"the winner is {winner}")  
        gamerunning = False    
                  

def checktie(game_board):
    global gamerunning
    if "_" not in game_board:
        printBoard(game_board)
        print("it is a tie!")
        gamerunning = False
                    
#switch the player
def switchplayer():
    global player
    if player == "X":
        player = "O"
    else:
        player ="X" 

#computer
def computer(game_board):
    while player  == "O":
        position = random.randint(0,8)
        if game_board[position] == "_":
            game_board[position] = player
            break
    switchplayer()
            
                    
        
#check for win or tie again
while gamerunning:
    printBoard(game_board)
    playerinput(game_board)
    checkifwin(game_board)
    checktie(game_board)
    switchplayer() 
    computer(game_board)
    checkifwin(game_board)
    checktie(game_board)