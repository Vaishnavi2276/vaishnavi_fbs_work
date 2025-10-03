class Shirt:
    size_increment = {
        "small": 0,
        "medium": 10,
        "large": 20,
        "xlarge": 30
    }
    def __init__(self, sid=None, sname=None, type_=None, price=None, size=None):
        self.sid = sid
        self.sname = sname
        self.type = type_
        self.base_price = price
        self.size = size

    def __del__(self):
        print(f"Shirt with ID {self.sid} is being deleted.")
    def calculate_price(self):
        if self.base_price is None or self.size is None:
            return None
        increment_percent = Shirt.size_increment.get(self.size.lower(), 0)
        return self.base_price + (self.base_price * increment_percent / 100)

    def ShowShirt(self):
        print(f"Shirt ID: {self.sid}")
        print(f"Shirt Name: {self.sname}")
        print(f"Type: {self.type}")
        print(f"Size: {self.size}")
        print(f"Price based on size: {self.calculate_price()}\n")

shirt1 = Shirt(301, "Casual Shirt", "Casual", 1000, "small")
shirt2 = Shirt(302, "Formal Shirt", "Formal", 1000, "medium")
shirt3 = Shirt(303, "Party Shirt", "Party", 1000, "large")
shirt4 = Shirt(304, "Office Shirt", "Formal", 1000, "xlarge")

shirt1.ShowShirt()
shirt2.ShowShirt()
shirt3.ShowShirt()
shirt4.ShowShirt()

del shirt1