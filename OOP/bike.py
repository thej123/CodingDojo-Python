class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    def ride(self):
        self.miles += 10
        print "Riding"
        return self
    def reverse(self):
        if (self.miles >= 5):
            self.miles -= 5
        print "Reversing"
        return self
    def displayInfo(self):
        print "Price: " , self.price
        print "Max_speed: " + self.max_speed
        print "Miles: " , self.miles
        return self


bike1 = Bike(200, "25mph")
print "bike 1 info"
bike1.ride().ride().ride().reverse().displayInfo()

bike2 = Bike(300,"30mph")
print "bike 2 info"
bike2.ride().ride().reverse().reverse().displayInfo()

bike3 = Bike(400,"35mph")
print "bike 3 info"
bike3.reverse().reverse().reverse().displayInfo()