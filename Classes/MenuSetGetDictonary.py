class Menu:

    def __init__(self):
        self.count = 0
        self.menu_items = dict()

    def add_item(self, item, price):
        self.menu_items[item] = price

    def set_item(self, item, price):
        for k, v in self.menu_items.items():
            if k == item:
                self.menu_items[item] = price
                return list(self.menu_items.items())[self.count]
            self.count += 1

    def get_item(self, item):
        for i, v in self.menu_items.items():
            if i == item:
                return {i: v}

    def show(self):
        return self.menu_items


m = Menu()

m.add_item("idly", 20)
m.add_item("vada", 30)

print("The added items are: ", m.show())

x = m.set_item("idly", 25)
print("The price of the item is idly is set to {0}".format(x))

a = m.get_item("idly")
print("The price of the item idly is {0}".format(a))

y = m.set_item("vada", 35)
print("The price of the item vada is set to {0}".format(y))

b = m.get_item("vada")
print("The price of the item vada is {0}".format(b))
