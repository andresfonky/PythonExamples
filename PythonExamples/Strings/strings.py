str1 = "okra is the closest thing to nylon i've ever eaten."
str2 = "pull the string, and it will follow wherever you wish."
str3 = "let out a little more string on your kite."
str4 = "every string is a different color, a different voice."
alphabet = "abcdefghijklmnopqrstuvwxyz"
vowels = 'aeiou'
atoms=("Hydrogen",1,"Helium",2,"Lithium",3,"Boron",5,"Carbon",6, "Oxygen",8)

def printstring():
    for i in range(0,len(str3)):
        print (str3[i], end="")
    print()

def printlen():
    for i in range(0,len(str3)):
        print (i, end="")
    print()

def printstring2():
    for i in str3:
        print (i, end="")
    print()
    
def printvowels():
    for i in str3:
        if i in vowels:
            print(i, end="")
    print()

def printifvowels():
    for i in range(0,len(str3)):
        if str3[i] in vowels:
            print(str4[i], end="")
        if len(str4) <= i+1:
            break;
    print()

def cyphstring():
    cyph = ""
    distance = 6
    for i in range(0, len(str1)):
        j = alphabet.find(str1[i])
        j = j+distance
        if str1[i] != " ":
            if j > len(alphabet)-1:
                j = j - len(alphabet)
            cyph = cyph + alphabet[j]
        else:
            cyph = cyph + " "
    print(cyph, end= "\n")

def descyphstring():
    cyphstr = "varr znk yzxotm gtj oz corr lurruc cnkxkbkx eua coyn"
    descyph = ""
    distance = 6
    for i in range(0, len(cyphstr)):
        j = alphabet.find(cyphstr[i])
        j = j - distance
        if cyphstr[i] != " ":
            if j < 0:
                j = j + len(alphabet)
            descyph = descyph + alphabet[j]
        else:
            descyph = descyph + " "
    print(descyph, end= "\n")