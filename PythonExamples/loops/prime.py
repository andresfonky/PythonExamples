print("Enter a number: ", end="")
isprime = ""

try:
    k = int(input())
    for n in range (2, int(k/2)): #Divide by all numbers
        if k%n == 0: # If the remainder is 0 then n
            isprime = "no" # divides evenly into K: not prime
            break
    else:
        isprime = "yes"

    print ("Is prime? ", isprime)

except:
    print("You must introduce a number")