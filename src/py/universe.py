class Item:
  subitems = []
  is_leaf = False 
  def get_amount():
    if is_final:
      return self.amount
    else:
      raise Exception("get_amount called on non leaf item.")
  def get_value():
    return sum([t.get_value() for t in self.subitems])
