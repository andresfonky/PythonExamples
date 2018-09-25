val = 21

def stickGame():
    global val
    while val > 0:
        displayState(val)
        move = getMove()
        val = val - move
        print("You took ", move, " and sticks leaving ", val, end="\n")
        if gameOver():
            print("You win")
            break;
        else:
            move = computerMove()
            val = val - move
            print("Computer took ", move, " and sticks leaving ", val, end="\n")
            if gameOver():
                print("Computer wins")
                break;


def displayState(val):
    while val > 0:
        if val > 6:
            print("0 0 0 0 0 0", end="\n")
            val = val - 6
        else:
            for i in range(0, val):
                print("0 ", end="")
            print()
            val = 0

def getMove():
    playboard = [5, 7, 9]
    userchoice = 0
    while userchoice <= 0 or userchoice > 3:
        try:
            userc = int(input("Your move: Choose number (1-%d) (0 to return): " % len(playboard)))
            userchoice = int(input("Your move: Take away how many? (1-3): "))
        except:
            print ("Sorry, your guess must be an integer.", end = "\n")

    return userchoice

def computerMove():
    global val
    n = val % 4
    if n<=0:
        return 1
    else:
        return n

def gameOver():
    global val
    if val == 0:
        return True
    return False

