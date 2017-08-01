for count in range(2,11):
    prime = False
    square = False
    for i in range(2,count):
        # if count == i*i:
        #     print count, "Bar"
        if count%i == 0:
            break
    else:
        prime = True
        print count, "Foo"

# for count in range(2,101):
    for i in range(2,count):
        if count == i*i:
            square = True
            print count, "Bar"

    if prime == False and square == False:
        print count, "Foobar"