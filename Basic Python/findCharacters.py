word_list = ['hollo','world','my','name','is','Anna']
char = 'o'

def findCaracters(li,character):

    new_list = []                           #intitalize an empty list
    for count in li:                        #goes thorugh every word
        if character in count:         #checks if any letter matches the 'character' given
            new_list.append(count)      #if it matches then adds that word to the new list
            # print "hello"
            
        
    print new_list

findCaracters(word_list,char)