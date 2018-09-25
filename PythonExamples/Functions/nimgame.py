
playboard = [5, 7, 9]
done = False
userMove = [-1, -1]

def play():
    global playboard
    while not done:
        printPlayBoard()
        userMove = askUserMove()
        updateGame(userMove)
        done = checkResult()
        if not done:
            computerMoves()
            done = checkResult()
            if done:
                print("Computer lose, you win")
        else:
            print("Sorry, you lose")

def printPlayBoard():
    global playboard
    for i in range(0,len(playboard)):
        print(i, ": ", end = "")
        for j in range(0, playboard[i]):
            print("|", end="")
        print("")

def askUserMove():
    global playboard

    back = False
    correct = False
    userchoicerow = 0
    userchoicenumber = 0

    while not correct:
        try:
            userchoicerow = int(input("Your move: Choose number (1-%d): " % len(playboard)))
            userchoicerow -= 1
            if 0 <= userchoicerow < len(playboard):
                if playboard[userchoicerow] > 0:
                    while not back or not correct:
                        try:
                            userchoicenumber = int(input("Your move: Choose number (1-%d) (0 to return): " % playboard[userchoicerow]))
                            if 1 <= userchoicenumber <= playboard[userchoicerow]:
                                print("a")
                                correct = True
                            elif userchoicenumber == 0:
                                print("b")
                                back = True
                            else:
                                print("Number must be between 1 and ", playboard[userchoicerow])
                        except:
                             print("Only numbers accepted")
                else:
                    print("Empty row")
            else:
                print("Number must be between 1 and ", len(playboard))
        except:
            print("Only numbers accepted")

    return [userchoicenumber, userchoicenumber]

def updateGame(userMove):
    global playboard
    playboard[userMove[0]] -= userMove[1]

def checkResult():
    global playboard
    finish = False
    for i in range (0, len(playboard)):
        if playboard[i] > 0:
            finish = False
            break
        else:
            finish = True
    return finish

def computerMoves():
    global playboard