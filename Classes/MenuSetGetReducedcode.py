class ItemAbsent(Exception):
    def __init__(self, item):
        f = open("log.txt", "a+")
        f.write("The item " + item + " not present in the list.\n")
        f.close()


class Menu:

    def __init__(self):
        self.menu_items = dict()

    def __setitem__(self, key, value):
        self.menu_items[key] = value

    def __delitem__(self, key):
        del self.menu_items[key]

    def __iter__(self):
        return self.menu_items

    def add_item(self, item, price):
        self.menu_items[item] = price

    def set_item(self, item, price):
        if item in self.menu_items:
            self.menu_items[item] = price
        else:
            raise ItemAbsent(item)

    def show(self):
        print(self.menu_items)


m = Menu()
m["pulav"] = 40

# del m["pulav"]


m.add_item("idly", 20)
m.add_item("vada", 30)
m.show()

try:
    m.set_item("idly", 25)
    m.show()
except ItemAbsent:
    pass

for i in m.__iter__():
    print(i)

try:
    m.set_item("dosa", 25)
    m.show()
except ItemAbsent:
    pass

try:
    m.set_item("poori", 25)
    m.show()
except ItemAbsent:
    pass

try:
    m.set_item("upma", 25)
    m.show()
except ItemAbsent:
    pass
