class Product(object):

    def __init__(self, price, item_name, weight, brand, cost):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.tax = 0.12
        self.status = "for sale"

    def sell(self):
        self.status = "sold"
        return self
    
    def add_tax(self):
        self.price = self.price + (self.price * self.tax)
        return self

    def return_item(self, reason, box):
        self.reason = reason
        self.box = box
        if (self.reason == "defective"):
            self.price = 0
            self.status = self.reason
        elif (self.box == "unopened"):
            self.status = "for sale"
        elif (self.box == "opened"):
            self.status = "used"
            self.price = self.price * 0.8
        return self

    def display_info(self):
        print "Price: $" + str(self.price)
        print "Item Name: " + str(self.item_name)
        print "Weight: " + str(self.weight) + "kg"
        print "Brand: " + str(self.brand)
        print "Cost: $" + str(self.cost)
        print "Status: " + str(self. status)

product1 = Product(100, "Mug", 10, "ford", 80)

# product1.display_info()
# product1.sell().display_info()
# product1.sell().add_tax().display_info()
# product1.sell().add_tax().return_item("defective", "opened").display_info()
product1.sell().add_tax().return_item("wrong item", "opened").display_info()
