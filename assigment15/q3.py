class Shirt():
    def __init__(self,id=100,name="max",type="casual",price=1000,size="small"):
        print("constructor calling")
        self.sid=id
        self.sname=name
        self.type=type
        self.price=price
        self.size=size

    def showShirt(self):
        print("shirt id:",self.sid)
        print("shirt sname:",self.sname)
        print("shirt type:",self.type)
        print("shirt price:",self.price)
        print("shirt size:",self.size)

    def __del__(self):
        print("destructor calling")

obj1=Shirt(101,"raymond","Formal",1500,"medium")
obj1.showShirt()
print("#########################")
obj2=Shirt()
obj2.showShirt()
