# Requirements

1. Create a vending machine that stores different products
2. Vending machine must be able to accept money from users and hold money (maintain a balance)
3. Vending machine dispenses items when the purchase is valid, and returns change if necessary
4. Machine must be able to reject invalid product requests (like if the product does not exist in the machine) and reject insufficient funds

# Classes

Machine

- Stores a list of products
- Orchestrates purchasing process: accepts money, review product requests, dispense items, returns change
  Product
- Name
- Cost
- Count
  User
- Name
- Balance
- Products
- Ability to dispense money
- Ability to request an item
