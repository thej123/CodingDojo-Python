profile = {"Name": "Thej", "Age": "26", "Country": "India", "language": "Python"}

def readDict (val):
    for count,data in val.iteritems():
        print "My ", count, "is ", data

readDict(profile)