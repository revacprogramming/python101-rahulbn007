class Menu:
  my_menu=[]
  def __init__(self,name='',price=0):
    self.my_menu.append((name,price))
  def __add__(self,a):
    self.my_menu.append((a[0],a[1]))
    return self
  def __str__(self):
    sd=self.my_menu[1:]
    return ("\n".join([str(a+' '+str(b)) for a,b in sd]))

  