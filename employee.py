class shopping_cart:
   
   cart = 0

   def __init__(self, item, total):
      self.item = item
      self.total  = total
      shopping_cart.cart += 1
   
   def count(self):
     print ("Total items %d" %shopping_cart.count)

   def display_cart(self):
      print ("item : ", self.item,  ", total: ", self.total)



emp1 = shopping_cart("apple", 20)
emp1.display_cart()
print("Total items " , shopping_cart.count)