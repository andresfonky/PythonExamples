a = 1
b = 2
i = 0

def aquilesvstoirtise():
    result = 0
    while i in range (0,20):
        control = (a/b)
        print (i, ": ", control, " +" , result)
        result += control
        b=b**2
        i += 1