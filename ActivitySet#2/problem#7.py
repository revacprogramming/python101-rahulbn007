class Menu:
  my_menu=[]
  def __init__(self,name='',price=0):
    self.my_menu.append((name,price))
  def __add__(self,a):
    return Menu(a[0],a[1])
  def __str__(self):
    sd=self.my_menu[1:]
  