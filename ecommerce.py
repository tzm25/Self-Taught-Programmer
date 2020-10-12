class Customer:
    def __init__(self,name,email):
        self.name = name
        self.email = email
        self.purchases = []

    def purchase(self, product , inventory):
        inventory_dict = inventory.inventory
        if product in inventory_dict:
            if inventory_dict[product] > 0:
                self.purchases.append(product)
                inventory_dict[product] -= 1
            else:
                print("Sorry!We are out of stock.")
        else:
            print("Sorry!We don't have that product")
    def print_purchase(self):
        print("The customer has purchased")
        for item in self.purchases:
            print(item.name)

class Product:
    def __init__(self,name,price):
        self.name = name
        self.price = price

class Inventory:
    def __init__(self):
        self.inventory = {}

    def add_product(self, product, quantity):
        if product not in self.inventory:
            self.inventory[product]= quantity
        else:
            self.inventory[product] += quantity

    def print_inventory(self):
        for key,value in self.inventory.items():
            print(key.name + ":" + str(value))

customer = Customer("TZM","tzmoe14ep@ytu.edu.mm")

mi = Product("Mi Band 5","$39" )
#print(mi.name)
#print(mi.price)

google_pixel4a = Product("Google Pixel 4a", "$349")

inventory = Inventory()
inventory.add_product(mi, 100)

inventory.add_product(google_pixel4a, 200)
inventory.print_inventory()

customer.purchase(mi, inventory)
customer.purchase(google_pixel4a, inventory)
inventory.print_inventory()
customer.print_purchase()