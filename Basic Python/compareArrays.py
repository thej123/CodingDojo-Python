list_one = [1,2,5,6,2]
list_two = [1,2,5,6,2]

list_one_2 = [1,2,5,6,5]
list_two_2 = [1,2,5,6,5,3]

list_one_3 = [1,2,5,6,5,16]
list_two_3 = [1,2,5,6,5]

list_one_4 = ['celery','carrots','bread','milk']
list_two_4 = ['celery','carrots','bread','cream']

def compareArrays(list_1, list_2):

    # for count in list_1,list_2:
    #     # if count(list_one)
    #     print count(list_1)

    if list_1 == list_2:
        print "The lists are the same."
    else:
        print "The list are not the same"

compareArrays(list_one, list_two)
compareArrays(list_one_2, list_two_2)
compareArrays(list_one_3, list_two_3)
compareArrays(list_one_4, list_two_4)