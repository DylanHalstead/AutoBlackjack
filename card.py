class Card:
  def __init__(self, card_string, top_left, bottom_right):
    self.card_string = card_string
    self.value_string = card_string[:-1]
    self.value = self.get_value()
    self.suit = card_string[-1]
    self.top_left = {'x': 0, 'y': 0}
    self.bottom_right = {'x': 0, 'y': 0}
    self.top_left = top_left
    self.bottom_right = bottom_right
  
  def get_value(self):
    if self.value_string.isdigit():
      return int(self.value_string)
    elif self.value_string == 'A':
      return 11
    else:
      return 10

  def set_ace_value(self, ace_value):
    if self.value_str == 'A':
      self.value = ace_value
  
  def __str__(self):
    return f"Card: {self.card_string}, Value String: {self.value_string}, Value: {self.value}, Suit: {self.suit}"