class Product(object):
    def __init__(self,price,item_name,weight,brand,cost):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = "for sale"

    def sell(self):
        self.status = "sold"
        return self

    def add_tax(self,tax):
        return self.price * (1.0 + tax)

    def return_prod(self,reason):
        if reason == "defective":
            self.status = "defective"
            self.price = 0
        elif reason == "in_box":
            self.status = "for sale"
        elif reason == "opened":
            self.status = "used"
            self.price = self.price * 0.8
        return self

    def display_info(self):
        print "Price:", self.price
        print "Item Name:", self.item_name
        print "Weight:", self.weight
        print "Brand:", self.brand
        print "Cost:", self.cost
        print "Status:", self.status
        print
        return self

product1 = Product(24.99,"Toaster","3lbs","NoNamo",15.35)
product1.sell().display_info().return_prod("opened").display_info().sell().display_info()
        
