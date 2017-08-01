l1 = ['magical unicorns',19,'hello',98.98,'world']
l2 = [2,3,1,7,4,12]
l3 = ['magical','unicorns']

def typeList(val):                  #Function typeList
    strOutput = ""                  # intializing 2 variable to keep count and adding strings.
    intOutput = 0

    for count in val:                       # go through each element
        # if isinstance(count,int):
            # print "hello"
        if type(count) == int:                 # check if the element is an integer
            intOutput += count                  # if it is integer then add it to the running count
        # elif isinstance(count,str):
        if type(count) == str:
            strOutput = strOutput + " " + count

    if intOutput and strOutput:
        print "The array you entered is of mixed type"
        print "Sum:", intOutput
        print "String:", strOutput
    elif intOutput:
        print "The array you entered is of integer type"
        print "Sum:", intOutput
    elif strOutput:
        print "The array you entered is of string type" 
        print "String:", strOutput

    
            



# typeList(l1)
typeList(l2)
typeList(l3)













#     if type(test[count]) == int:
#         intOutput += test[count]
    
#     if type(test[count]) == str:
#         strOutput += test[count]

# print intOutput
# print strOutput