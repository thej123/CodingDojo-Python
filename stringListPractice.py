words = "It's thanksgiving day. It's my birthday,too!"
print words.find("day")
wordsMonth = words.replace("day", "month", 1)
print wordsMonth

x=[2,54,-2,7,12,98]
print min(x)
print max(x)

x1=["hello",2,54,-2,7,12,98,"world"]
first = x1[0]
last = x1[-1]
print first
print last
newx1 = [first, last]
print newx1

x2 = [19,2,54,-2,7,12,98,32,10,-3,6]
x2.sort()
print x2

firstHalf = x2[:len(x2)/2]
secondHalf = x2[len(x2)/2:]
print firstHalf
print secondHalf

secondHalf.insert(0,firstHalf)
print secondHalf