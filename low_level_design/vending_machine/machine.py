from product import Product
from person import Person
class Machine:
    def __init__(self, balance: float, products: dict[Product, int] = None):
        self.balance = balance
        if products is None:
            products = {}

        self.products = products


    def add_products(self, products: list[Product]):
        """ Adds list of products to machine """
        for product in products:
            if product in self.products:
                self.products[product] += 1
            else:
                self.products[product] = 1
    
    def get_products(self):
        """ Return product dict """
        return self.products
    
    def orchestrate_purchase(self, person: Person, amount: float, products: list[Product]):
        if self.accept_money(amount):
            total = 0
            for p in products:
                total += p.cost
            
            if total > amount:
                return False
            
            change = amount - total
            self.balance += amount
            self.balance -= change
            person.balance -= amount
            person.balance += change

            for product in products:
                if product in person.products:
                    person.products[product] += 1
                else:
                    person.products[product] = 1

            for product in products:
                if product in self.products:
                    self.products[product] -= 1
                else:
                    del self.products[product]

            return True
    
    def accept_money(self, amount: float):
        if amount > 100:
            return False
        
        min_price = min(product.cost for product in self.products)

        if amount < min_price:
            return False
        
        return True  

machine = Machine(0, None)
print(machine)
ginger_ale = Product("Ginger Ale", 2.50)
coke = Product("Coke", 2.00)
machine.add_products([ginger_ale, coke, coke])
print(machine.get_products())
ruitao = Person("Ruitao", 10.00, None)
machine.orchestrate_purchase(ruitao, 5.00, [coke])
print(machine.get_products())



        
