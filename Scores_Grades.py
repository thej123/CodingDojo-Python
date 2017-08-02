def grades():
    import random
    random_num = random.randint(60,101)

    if 60 <= random_num <= 69:
        print "Score: ", random_num , "; Your grade is D."
    elif 70 <= random_num <= 79:
        print "Score: ", random_num , "; Your grade is C."
    elif 80 <= random_num <= 89:
        print "Score: ", random_num , "; Your grade is B."
    else:
        print "Score: ", random_num , "; Your grade is A."

grades()