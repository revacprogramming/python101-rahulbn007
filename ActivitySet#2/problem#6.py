class Menu:
  my_menu=[]
  def add(self,name,price):
    self.my_menu.append((name,price))
  def show(self):
    for a,b in self.my_menu:
      print(a,b)
    
  
m = Menu()  # Menu is a class
m.add("idly", 10)
m.add("vada", 20)

