class menu:
    def __init__(self):
        self.menuitems = []

    def additems(self, items, pricevalue):
        self.menuitems.append(items)
        self.menuitems.append(pricevalue)
        #return self.menuitems

    def show(self):
         return self.menuitems

m = menu()
m1 = menu()
m.additems("Idly",10)
m.additems("Vada",20)

m1.additems("Dosa",30)


print(m.show())
print(m1.show())
#
#i=m.setprice("idly",30)
#print(i)


#m.show()
#m1.show()
