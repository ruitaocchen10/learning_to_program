from product import Product

class Machine:
    def __init__(self, balance: int, products = None):
        self.balance = balance
        if products is None:
            products = []

        self.products = products


    def add_products(self, products: list[Product]):
        """ Adds list of products to machine """
        for product in products:
            self.products.append(product)
    
    def get_products(self):
        """ Return product list """
        return self.products
    

machine = Machine(0, None)
products = machine.get_products()
print(products)
new_products = [ Product("Coke", 2.00, 2), Product("Pepsi", 2.50, 3) ]
machine.add_products(new_products)
print(products)

        
