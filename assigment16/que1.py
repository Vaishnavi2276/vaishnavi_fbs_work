class Book:
    count = 0
    def __init__(self, bid=None, bname=None, price=None, author=None):
        self.bid = bid
        self.bname = bname
        self.price = price
        self.author = author
        Book.count += 1
    def __del__(self):
        print(f"Book with ID {self.bid} is being deleted.")
        Book.count -= 1
    def ShowBook(self):
        print(f"Book ID: {self.bid}")
        print(f"Book Name: {self.bname}")
        print(f"Price: {self.price}")
        print(f"Author: {self.author}")
        print(f"Total Books Created: {Book.count}\n")

book1 = Book(101, "Python Programming", 500, "John Doe")
book2 = Book()  

book1.ShowBook()
book2.ShowBook()

book3 = Book(102, "Data Structures", 450, "Jane Smith")
book3.ShowBook()

del book1
print(f"Books remaining: {Book.count}")