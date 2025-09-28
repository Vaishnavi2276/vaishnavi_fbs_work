class Book():
    def __init__(self,id=500,name="Indica",price=600,author="Megasthenes"):
        print("constructor calling")
        self.bid=id
        self.name=name
        self.price=price
        self.author=author

    def showBook(self):
        print("Book id:",self.bid)
        print("Book name:",self.name)
        print("Book price:",self.price)
        print("Book of the author:",self.author)

    def __del__(self):
        print("destructor calling")

obj1=Book(102,"Indica",600,"Megasthenes")
obj1.showBook()
print("###################")
obj2=Book()
obj2.showBook()