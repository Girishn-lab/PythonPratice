class ItemAbsent(Exception):
    pass


class Menu:

    def __init__(self):
        self.menu_items = dict()

    def add_item(self, item, price):
        self.menu_items[item] = price

    def set_item(self, item, price):
        f = open("log.txt", "a+")
        try:
            if item in self.menu_items:
                self.menu_items[item] = price
            else:
                raise ItemAbsent
        except ItemAbsent:
            f.write("The item " + item + " not present in the list.\n")
        finally:
            f.close()

    def show(self):
        print(self.menu_items)


m = Menu()

m.add_item("idly", 20)
m.add_item("vada", 30)
m.show()

m.set_item("idly", 25)
m.show()

m.set_item("dosa", 25)
m.show()

m.set_item("poori", 25)
m.show()

m.set_item("upma", 25)
m.show()
