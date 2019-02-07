'''
create simple class
attributes - variables
methods - function working usually with attributes
'''
class CashRegister:
    def __init__(self):
        #Attributes
        self.items = 0
        self.price = 0
    #Methods
    def update_register(self,price):
        self.items = self.items + 1
        self.price = self.price + price
    def display_register(self):
        return print('The number of items ',self.items,'\nTotal price $',self.price)
    def clear_register(self):
        self.items = 0
        self.price = 0
register1 = CashRegister()
register1.update_register(1.95)
register1.update_register(.65)
register1.update_register(99.99)
register1.update_register(25000)
print('Clearing register 1...')
register1.clear_register()
print('Damains list')
register1.update_register(2.09)
register1.display_register()

register2=CashRegister()
register2.update_register(500)
register2.display_register()