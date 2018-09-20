class rootsquare(object):
    """description of class"""

def root (x): # Compute the square root of x
    y = x # First guess: too big, probably
    check = 1
    while check > 0.00001: # Iterate20 time
        ypast = y
        y = (y + x/y)/2.0 # Average the prior guess and x/y
        check = ypast - y
        ypast = y
        print (y, " con diferencia de ", check)
    return y # Return the last guess
