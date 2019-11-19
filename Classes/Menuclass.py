class menu:
    def __init__(self, items, price):
        self.items = items
        self.price = price
        self.menuitems = []

    def additems(self):
        self.menuitems.append(self.items)
        self.menuitems.append(self.price)

    def show(self):
        print("The item is {0} and price is {1} ".format(self.items, self.price))

m = menu("Idly",10)
m1 = menu("Vada",20)
m.additems()
m.show()
#print("The item is {0} and price is {1} ".format(m.items, m.price))

m1.additems()
m1.show()
#print("The item is {0} and price is {1} ".format(m1.items, m1.price))

