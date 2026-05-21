from product import Product

class Person:
    def __init__ (self, name: str, balance: float, products: dict[Product, int] = None):
        self.name = name
        self.balance = balance
        if products is None:
            products = {}

        self.products = products

    