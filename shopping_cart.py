""" The shopping cart adds items and no of items to the cart.If the new item is similar to basket, it is discarded.
      But if the new item is new to cart, it is added to the cart
"""

class shopping_cart():
    "The shopping cart add and remove items from the cart"


    def __init__(self, item):
        self.cart   =   {}
        self.item = item

    def add_item(self, item, quantity):
        if not item in self.cart:
            self.quantity = quantity
            print(item, "added",quantity,"kgs ")
        else:
            print(item, "is already in the cart")

    def remove_item(self, item):

        if item in self.cart:
            del self.cart[item]
            print(item, " removed")
        else:
            print(item, " is not in the cart")
   
    def update_item(self,item, quantity):
        if not item in self.cart:
            self.update(cart.quantity)
            print("values updated:",self.cart)
        else:
            print("Not added")


if __name__ == "__main__":
    cart_obj1 = shopping_cart("apple")
    cart_obj1.add_item("apple ", 10)

    cart_obj2 = shopping_cart("mango")
    cart_obj2.add_item("mango", 20)

    cart_obj3 = shopping_cart("apple")
    cart_obj3.remove_item("apple")
