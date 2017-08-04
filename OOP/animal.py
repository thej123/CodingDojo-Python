class Animal(object):

    def __init__(self, name):                       #takes in name and health amount
        self.name = name
        self.health = 100
    
    def walk(self):                                         #walking takes away 1 health
        if (self.health > 0):
            self.health -= 1
        else:
            print "You have no health to walk"
        return self
    
    def run(self):                                          #running takes away 5 health
        if (self.health > 4):
            self.health -= 5
        else:
            print "You dont have enough health to run"
        return self
    
    def display_health(self):                               #displays health
        print "Name: " + str(self.name)
        print "Health: " + str(self.health)
        return self
    
animal1 = Animal("cat")
animal1.walk().walk().walk().run().run().display_health()

class Dog(Animal):

    def __init__(self, name):                               #sets only one parameter unlike parent
        super(Dog, self).__init__(name)
        self.health = 150
    
    def pet(self):
        self.health += 5
        return self

dog1 = Dog("leapord")
dog1.walk().walk().walk().run().run().pet().display_health()

class Dragon(Animal):

    def __init__(self, name):                               #sets only one parameter unlike parent
        super(Dragon, self).__init__(name)
        self.health = 170
    
    def fly(self):
        if (self.health > 9):
            self.health -= 10
        else:
            print "You dont have enough health"
        return self
    
    def display_health(self):
        super(Dragon, self).display_health()
        print "I am a Dragon"
        return self

dragon1 = Dragon("Drogo")
dragon1.walk().run().fly().display_health()

# animal2 = Dog("catty")
# animal2.display_health()