# prints all the odd numbers from 1 to 1000
print "all odd number"
for count in range(1, 1001, 2):
    print count

# prints all the multiples of 5 from 5 to 1,000,000.
print "all multiples of 5"
for count in range(5, 1000001, 5):
    print count

a = [1,2,5,10,255,3]
print "sum : ", sum(a)               #sum of the list 'a'

print "average : ", sum(a)/len(a)         #average of the list 'a'