setprice = None


class Menu:

    def __init__(self):
        self.menu_items = []

    def add_items(self, item, price):
        self.menu_items.append(item)
        self.menu_items.append(price)

    def show(self):
        return self.menu_items

    def set_price(self, item, setprice):
        for k, v in enumerate(self.menu_items):
            if v == item:
                self.menu_items.insert(k + 1, setprice)
                self.menu_items.pop(k + 2)

    def get_price(self, item):
        for i, v in enumerate(self.menu_items):
            if v == item:
                return self.menu_items[i + 1]


m = Menu()

m.add_items("idly", 20)
print(m.show())

m.set_price("idly", 40)
print(m.show())

m.get_price("idly")
print(m.show())

m.add_items("vada", 50)
print(m.show())

m.set_price("vada", 60)
print(m.show())

m.get_price("vada")
print(m.show())

# m.add_items("dosa",35)
# print(m.show())

# m.set_price("dosa",40)
# print(m.show())

# m.get_price("dosa")
# print(m.show())
