class Product:
    discount = 0.0

    def __init__(self, pid=None, pname=None, price=None, quantity=None):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.quantity = quantity
    def __del__(self):
        print(f"Product with ID {self.pid} is being deleted.")

    def ShowProduct(self):
        print(f"Product ID: {self.pid}")
        print(f"Product Name: {self.pname}")
        print(f"Price: {self.price}")
        print(f"Quantity: {self.quantity}")
        print(f"Discount: {Product.discount}%\n")

    def apply_discount(self):
        if self.price is not None:
            discounted_price = self.price - (self.price * Product.discount / 100)
            return discounted_price
        else:
            return None

    @classmethod
    def set_discount(cls, discount_value):
        cls.discount = discount_value


Product.set_discount(10)  

prod1 = Product(201, "Laptop", 50000, 2)
prod2 = Product()  

prod1.ShowProduct()
print(f"Price after discount: {prod1.apply_discount()}\n")

prod2.ShowProduct()
prod2.pid = 202
prod2.pname = "Mouse"
prod2.price = 500
prod2.quantity = 5
print(f"Price after discount: {prod2.apply_discount()}\n")

del prod1