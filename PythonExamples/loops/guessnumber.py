choice = 7
guessed = False

def guessnumber():
    while not guessed:
        print ("Please guess a number between 1 and 10: ")
        try:
            playerchoice = int(input())
            guessed = True
        except:
            print ("Sorry, your guess must be an integer.")
        if playerchoice<0 or playerchoice>10: # Is the guess in 1..10?
            print ("Your guess was",playerchoice,"which is out of range.")
            guessed = False # Nope. Guess again

    if choice == playerchoice:
        print ("You win!")
    else:
        print ("Sorry, you lose.")