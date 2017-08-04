# for count in range(1,13):
#         print "x 1 2 3 4 5 6 7 8 9 10 11 12"

for row in range(1,13):
    count = ""
    for column in range(1,13):
        count += "     " + str(row*column)
    print count

