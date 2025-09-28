class Product():
    def __init__(self,id=500, name="TV",price= 6000,quantity=1):
        print("construcur calling")
        self.pid=id
        self.pname=name
        self.price=price
        self.quantity=quantity

    def showProduct(self):
        print("product id:",self.pid)
        print("product name:",self.pname)
        print("product price:",self.price)
        print("product qunantity:",self.quantity)

    def __del__(self):
        print("destructor calling")

obj1=Product(500, "TV",6000,1)
obj1.showProduct()
print("##################")
obj2=Product()
obj2.showProduct()


        