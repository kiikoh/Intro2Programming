# File: itemDePace.py
class Item:
    """Models an item in a store"""

    def __init__(self, name, quantity, price):
        """Makes an item with a name, price, and quantity"""
        self.myName = name
        self.myQuantity = quantity
        self.myPrice = price

    def __str__(self):
        """Returns a string representation of the item"""
        return "{} x {}, ${:0.2f} each".format(self.myQuantity, self.myName, self.myPrice)

    def getName(self):
        """Gets the name of the item"""
        return self.myName

    def setName(self, name):
        """Sets the name of the item"""
        self.myName = name

    def getQuantity(self):
        """Gets the quantity of the item"""
        return self.myQuantity

    def setQuantity(self, quantity):
        """Sets the quantity of the item"""
        self.myQuantity = quantity

    def getPrice(self):
        """Gets the price of the item"""
        return self.myPrice

    def setPrice(self, price):
        """Sets the price of the item"""
        self.myPrice = price
