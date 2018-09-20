'''A calculator company produces a scientific calculator and a graphing calculator. Long-term projections indicate an expected demand of at
least 100 scientific and 80 graphing calculators each day. Because of limitations on production capacity, no more than 200 scientific and 
170 graphing calculators can be made daily. To satisfy a shipping contract, a total of at least 200 calculators much be shipped each day.
If each scientific calculator sold results in a $2 loss, but each graphing calculator produces a $5 profit, how many of each type should 
be made daily to maximize net profits?'''

#100 <= s <= 200
#80 <= g <= 170
#Also: s + g > 200, or g > 200 - s
#Finally, the profit, which is to be maximized, is: P = –2s + 5g

# Range for s is x0 .. x1
# Range for g is y0 .. y1
# s+g must be >= sum

def minmax():
    c = searchmax (100, 200, 80, 170, 200)
    print (c)

def searchmax (x0, x1, y0, y1, sum):
    pmax = 0
    ps = -100
    pg = -100
    for s in range (x0, x1+1): # For all possible s
        for g in range (y0, y1+1): # For all possible g
            if s+g >= sum: # Condition is ok?
                p = profit(s, g) # Calculate the profit.
                if p>=pmax: # Best so far?
                    pmax = p # Yes.
                    ps = s # Save it and
                    pg = g # the parameters
    return ( (ps, pg) )

def profit (s, g):
    return -2*s + 5*g

