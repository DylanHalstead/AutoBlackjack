from card import Card

# The key is the players hand sum and the value is the dealers up card
decision_table = {
  'hard': {
    5: {2: 'hit', 3: 'hit', 4: 'hit', 5: 'hit', 6: 'hit', 7: 'hit', 8: 'hit', 9: 'hit', 10: 'hit', 'A': 'hit'},
    6: {2: 'hit', 3: 'hit', 4: 'hit', 5: 'hit', 6: 'hit', 7: 'hit', 8: 'hit', 9: 'hit', 10: 'hit', 'A': 'hit'},
    7: {2: 'hit', 3: 'hit', 4: 'hit', 5: 'hit', 6: 'hit', 7: 'hit', 8: 'hit', 9: 'hit', 10: 'hit', 'A': 'hit'},
    8: {2: 'hit', 3: 'hit', 4: 'hit', 5: 'hit', 6: 'hit', 7: 'hit', 8: 'hit', 9: 'hit', 10: 'hit', 'A': 'hit'},
    9: {2: 'hit', 3: 'double down', 4: 'double down', 5: 'double down', 6: 'double down', 7: 'hit', 8: 'hit', 9: 'hit', 10: 'hit', 'A': 'hit'},
    10: {2: 'double down', 3: 'double down', 4: 'double down', 5: 'double down', 6: 'double down', 7: 'double down', 8: 'double down', 9: 'double down', 10: 'hit', 'A': 'hit'},
    11: {2: 'double down', 3: 'double down', 4: 'double down', 5: 'double down', 6: 'double down', 7: 'double down', 8: 'double down', 9: 'double down', 10: 'double down', 'A': 'hit'},
    12: {2: 'hit', 3: 'hit', 4: 'stand', 5: 'stand', 6: 'stand', 7: 'hit', 8: 'hit', 9: 'hit', 10: 'hit', 'A': 'hit'},
    13: {2: 'stand', 3: 'stand', 4: 'stand', 5: 'stand', 6: 'stand', 7: 'hit', 8: 'hit', 9: 'hit', 10: 'hit', 'A': 'hit'},
    14: {2: 'stand', 3: 'stand', 4: 'stand', 5: 'stand', 6: 'stand', 7: 'hit', 8: 'hit', 9: 'hit', 10: 'hit', 'A': 'hit'},
    15: {2: 'stand', 3: 'stand', 4: 'stand', 5: 'stand', 6: 'stand', 7: 'hit', 8: 'hit', 9: 'hit', 10: 'hit', 'A': 'hit'},
    16: {2: 'stand', 3: 'stand', 4: 'stand', 5: 'stand', 6: 'stand', 7: 'hit', 8: 'hit', 9: 'hit', 10: 'hit', 'A': 'hit'},
    17: {2: 'stand', 3: 'stand', 4: 'stand', 5: 'stand', 6: 'stand', 7: 'stand', 8: 'stand', 9: 'stand', 10: 'stand', 'A': 'stand'},
    18: {2: 'stand', 3: 'stand', 4: 'stand', 5: 'stand', 6: 'stand', 7: 'stand', 8: 'stand', 9: 'stand', 10: 'stand', 'A': 'stand'},
    19: {2: 'stand', 3: 'stand', 4: 'stand', 5: 'stand', 6: 'stand', 7: 'stand', 8: 'stand', 9: 'stand', 10: 'stand', 'A': 'stand'},
    20: {2: 'stand', 3: 'stand', 4: 'stand', 5: 'stand', 6: 'stand', 7: 'stand', 8: 'stand', 9: 'stand', 10: 'stand', 'A': 'stand'},
  },
  'soft': {
    13: {2: 'hit', 3: 'hit', 4: 'hit', 5: 'double down', 6: 'double down', 7: 'hit', 8: 'hit', 9: 'hit', 10: 'hit', 'A': 'hit'},
    14: {2: 'hit', 3: 'hit', 4: 'hit', 5: 'double down', 6: 'double down', 7: 'hit', 8: 'hit', 9: 'hit', 10: 'hit', 'A': 'hit'},
    15: {2: 'hit', 3: 'hit', 4: 'double down', 5: 'double down', 6: 'double down', 7: 'hit', 8: 'hit', 9: 'hit', 10: 'hit', 'A': 'hit'},
    16: {2: 'hit', 3: 'hit', 4: 'double down', 5: 'double down', 6: 'double down', 7: 'hit', 8: 'hit', 9: 'hit', 10: 'hit', 'A': 'hit'},
    17: {2: 'hit', 3: 'double down', 4: 'double down', 5: 'double down', 6: 'double down', 7: 'hit', 8: 'hit', 9: 'hit', 10: 'hit', 'A': 'hit'},
    18: {2: 'stand', 3: 'double down', 4: 'double down', 5: 'double down', 6: 'double down', 7: 'stand', 8: 'stand', 9: 'hit', 10: 'hit', 'A': 'hit'},
    19: {2: 'stand', 3: 'stand', 4: 'stand', 5: 'stand', 6: 'stand', 7: 'stand', 8: 'stand', 9: 'stand', 10: 'stand', 'A': 'stand'},
    20: {2: 'stand', 3: 'stand', 4: 'stand', 5: 'stand', 6: 'stand', 7: 'stand', 8: 'stand', 9: 'stand', 10: 'stand', 'A': 'stand'},
  },
  'pair': {
    2: {2: 'split', 3: 'split', 4: 'split', 5: 'split', 6: 'split', 7: 'split', 8: 'split', 9: 'split', 10: 'split', 'A': 'split'},
    4: {2: 'split', 3: 'split', 4: 'split', 5: 'split', 6: 'split', 7: 'split', 8: 'hit', 9: 'hit', 10: 'hit', 'A': 'hit'},
    6: {2: 'split', 3: 'split', 4: 'split', 5: 'split', 6: 'split', 7: 'split', 8: 'hit', 9: 'hit', 10: 'hit', 'A': 'hit'},
    8: {2: 'hit', 3: 'hit', 4: 'hit', 5: 'split', 6: 'split', 7: 'hit', 8: 'hit', 9: 'hit', 10: 'hit', 'A': 'hit'},
    10: {2: 'double down', 3: 'double down', 4: 'double down', 5: 'double down', 6: 'double down', 7: 'double down', 8: 'double down', 9: 'double down', 10: 'hit', 'A': 'hit'},
    12: {2: 'split', 3: 'split', 4: 'split', 5: 'split', 6: 'split', 7: 'hit', 8: 'hit', 9: 'hit', 10: 'hit', 'A': 'hit'},
    14: {2: 'split', 3: 'split', 4: 'split', 5: 'split', 6: 'split', 7: 'split', 8: 'hit', 9: 'hit', 10: 'hit', 'A': 'hit'},
    16: {2: 'split', 3: 'split', 4: 'split', 5: 'split', 6: 'split', 7: 'split', 8: 'split', 9: 'split', 10: 'split', 'A': 'split'},
    18: {2: 'split', 3: 'split', 4: 'split', 5: 'split', 6: 'split', 7: 'stand', 8: 'split', 9: 'split', 10: 'stand', 'A': 'stand'},
    20: {2: 'stand', 3: 'stand', 4: 'stand', 5: 'stand', 6: 'stand', 7: 'stand', 8: 'stand', 9: 'stand', 10: 'stand', 'A': 'stand'},
  }
}

class Hand:
  def __init__(self):
    self.cards = []
  
  def __init__(self, cards: list[Card]):
    self.cards = cards

  def add_card(self, card: Card):
    self.cards.append(card)

  def get_sum(self):
    hand_sum = 0
    for card in self.cards:
      hand_sum += card.value
    return hand_sum
  
  def is_soft(self):
    for card in self.cards:
      if card.value == 11:
        return True
    return False
  
  def is_pair(self):
    return len(self.cards) == 2 and self.cards[0].value == self.cards[1].value
  
  def calculate_best_action(self, dealer_up_card: Card):
    pass

  def __str__(self) -> str:
    return f"Hand: {self.cards}"