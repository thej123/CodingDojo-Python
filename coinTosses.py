def coinToses():
    import random
    
    heads = 0
    tails = 0
    attempt = 0

    for count in range (1,11):
        random_num = random.randint(1,2)
        attempt += 1

        if random_num == 1:
            heads += 1
            print "Attempt #", attempt, ": Throwing a coin... It's a head! ... Got " , heads , "head(s) so far and " , tails , "tail(s) so far"

        else:
            tails += 1
            print "Attempt #", attempt, ": Throwing a coin... It's a tail! ... Got " , heads , "head(s) so far and " , tails , "tail(s) so far"
       

coinToses()