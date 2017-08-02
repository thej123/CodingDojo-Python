def oddEven():
    for count in range(1,10):
        if count%2!=0:
            print "Number is ", count , ". This is an odd number."
        else:
            print "Number is ", count , ". This is an even number."
oddEven()

def multiply(arr,num):
    # b = multiply(arr,5)
    # b = []
    for count in range (0, len(arr)):
        arr[count] *= num
    return arr


# arr = [2,4,10,16]
# # num = 5
# b = multiply(arr,5)
# multiply(arr,num)

def hacker(arrTwo):
    newArr = []
    print repr(arrTwo)
    for count in arrTwo:   # count = 6
        newnewArr = []
        for x in range (0, count):
            newnewArr.append(1)
        # print newnewArr 
            # print "hello"
        newArr.append(newnewArr)
    return newArr



# arrTwo = [6,12,15]
print "hello"
x = hacker(multiply([2, 4, 5], 3))
print x
print "hello"
# x = hacker(multiply(arr)
# x = hacker([6,12,15])
# x = hacker(arrTwo)

