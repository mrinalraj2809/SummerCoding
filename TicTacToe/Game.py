import random
from time import sleep
from  os import system,name
def printBoard(value):
    sleep(0.300)
    #for windows os.name is 'nt'
    if name == 'nt':
        system('cls')
    #for linux os.name is 'posix'
    else:
        system('clear')
    print("\t_________________________")
    print("\t|   %(7)s   |   %(8)s   |   %(9)s   |"%{'7':value[7],'8':value[8],'9':value[9]})
    print("\t|   %(4)s   |   %(5)s   |   %(6)s   | " % {'4':value[4],'5':value[5],'6':value[6]})
    print("\t|   %(1)s   |   %(2)s   |   %(3)s   |"%{'1':value[1],'2':value[2],'3':value[3]})
    print("\t|_______|_______|_______|")
def chooseFirst():
    return random.randint(1,2)

def spaceCheck(value,mark):
    if value[mark] == ' ':
        return True
    else:
        return False
def checkWin(value):
    if value[1] == value[2] == value[3] and value [3]!= ' ':
        return True
    elif value[1] == value[4] ==value[7]and value [7]!= ' ':
        return True
    elif value[1] == value[5] == value [9]and value [9]!= ' ':
        return True
    elif value[2] == value[5] == value [8]and value [8]!= ' ':
        return True
    elif value[3] == value[6] == value [9]and value [9]!= ' ':
        return True
    elif value[3] == value[5] == value [7]and value [7]!= ' ':
        return True
    elif value[4] == value[5] == value [6]and value [6]!= ' ':
        return True
    elif value[7] == value[8] == value [9]and value [9]!= ' ':
        return True
    else:
        return False

def isBoardFull(value):
    """
    if(" " not in value):
        return True
    else:
        return False
    """
    for i in range(1,10):
        if value[i] is " ":
            return False
    else:
        return True
def menu():
    print("1. Play Again \n2. Exit")
    choice = int(input("Enter the choice : "))
    if choice == 1:
        getInput()
def replay():
    print("1. Play Again \n2. Exit")
    choice = int(input("Enter the choice : "))
    if choice == 1:
        return True
    else:
        return False
flag = 0
def getInput():
    global flag
    value = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    printBoard(value)
    playerTurn = chooseFirst()  #player 1 cross"X" and player 2 "O"
    while(True):
        if flag == 1:
            break
        mark = input("Player "+str(playerTurn)+" Enter the number in the keypad to mark : ")
        if  mark not in ['1','2','3','4','5','6','7','8','9'] or (spaceCheck(value, int(mark)) == False):
            print("Please re-enter ")
            continue
        mark = int(mark)
        if playerTurn == 1:
            value[mark] = 'X'
        else:
            value[mark] = 'O'
        printBoard(value)
        if checkWin(value)==True :
            print("Player ",playerTurn, " is the winner\n")
            print("1. Play Again \n2. Exit")
            choice = int(input("Enter the choice : "))
            if choice == 1:
                getInput()
            else:
                print("Exiting...")
                break
        if playerTurn ==1 :
            playerTurn =2
        else :
            playerTurn =1
        if (isBoardFull(value)):
            print("Draw\n")
            print("1. Play Again \n2. Exit")
            choice = int(input("Enter the choice : "))
            if choice == 1:
                getInput()
            else:
                print("Exiting...")
                flag = 1
                break
getInput()
