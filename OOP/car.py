class Car(object):

    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if (self.price > 10000):
            self.tax = 0.15
        else:
            self.tax = 0.12
        self.display_all()


    def display_all(self):
        print "Price: " + str(self.price)
        print "Speed: " + str(self.speed)
        print "Fuel: " + str(self.fuel)
        print "Mileage: " + str(self.mileage)
        print "Tax: " + str(self.tax)

        return self

print "Car 1 info"
car1 = Car(2000, "35mph", "Full", "15mpg")
print "Car 2 info"
car2 = Car(2000, "5mph", "Not Full", "105mpg")
print "Car 3 info"
car3 = Car(2000, "15mph", "Kind of Full", "95mpg")
print "Car 4 info"
car4 = Car(2000, "25mph", "Full", "25mpg")
print "Car 5 info"
car5 = Car(2000, "45mph", "Empty", "25mpg")
print "Car 6 info"
car6 = Car(20000000, "35mph", "Empty", "15mpg")