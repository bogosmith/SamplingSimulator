class Item:
  subitems = []
  is_leaf = False 
  amount = 0
  name = ""
  def __init__(self, name):
    self.name = name
  def get_value(self):
    if self.is_leaf:
      return self.amount
    else:
      return sum([t.get_value() for t in self.subitems])
  def display(self, indent):
      leading_space = "".join([" " for t in range(0,indent)])
      subitems = "".join([t.display(indent + 2) for t in self.subitems])
      result = leading_space + self.name + " " + str(self.get_value()) + "\n" + subitems
      return result
if __name__ == "__main__":
  i = Item("aa")
  i.is_leaf = True
  i.amount = 100
  j = Item("bb")
  j.is_leaf = True
  j.amount = 20.20
  k = Item("higher")
  k.subitems = [i,j]
  #print(i.get_amount())
  print(k.display(0))
