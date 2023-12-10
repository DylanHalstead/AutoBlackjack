from card import Card

# The key is the players hand sum and the value is the dealers up card
decision_table = {
  'hard': {
    5: {2: 'hit', 3: 'hit', 4: 'hit', 5: 'hit', 6: 'hit', 7: 'hit', 8: 'hit', 9: 'hit', 10: 'hit', 11: 'hit'},
    6: {2: 'hit', 3: 'hit', 4: 'hit', 5: 'hit', 6: 'hit', 7: 'hit', 8: 'hit', 9: 'hit', 10: 'hit', 11: 'hit'},
    7: {2: 'hit', 3: 'hit', 4: 'hit', 5: 'hit', 6: 'hit', 7: 'hit', 8: 'hit', 9: 'hit', 10: 'hit', 11: 'hit'},
    8: {2: 'hit', 3: 'hit', 4: 'hit', 5: 'hit', 6: 'hit', 7: 'hit', 8: 'hit', 9: 'hit', 10: 'hit', 11: 'hit'},
    9: {2: 'hit', 3: 'double down', 4: 'double down', 5: 'double down', 6: 'double down', 7: 'hit', 8: 'hit', 9: 'hit', 10: 'hit', 11: 'hit'},
    10: {2: 'double down', 3: 'double down', 4: 'double down', 5: 'double down', 6: 'double down', 7: 'double down', 8: 'double down', 9: 'double down', 10: 'hit', 11: 'hit'},
    11: {2: 'double down', 3: 'double down', 4: 'double down', 5: 'double down', 6: 'double down', 7: 'double down', 8: 'double down', 9: 'double down', 10: 'double down', 11: 'hit'},
    12: {2: 'hit', 3: 'hit', 4: 'stand', 5: 'stand', 6: 'stand', 7: 'hit', 8: 'hit', 9: 'hit', 10: 'hit', 11: 'hit'},
    13: {2: 'stand', 3: 'stand', 4: 'stand', 5: 'stand', 6: 'stand', 7: 'hit', 8: 'hit', 9: 'hit', 10: 'hit', 11: 'hit'},
    14: {2: 'stand', 3: 'stand', 4: 'stand', 5: 'stand', 6: 'stand', 7: 'hit', 8: 'hit', 9: 'hit', 10: 'hit', 11: 'hit'},
    15: {2: 'stand', 3: 'stand', 4: 'stand', 5: 'stand', 6: 'stand', 7: 'hit', 8: 'hit', 9: 'hit', 10: 'hit', 11: 'hit'},
    16: {2: 'stand', 3: 'stand', 4: 'stand', 5: 'stand', 6: 'stand', 7: 'hit', 8: 'hit', 9: 'hit', 10: 'hit', 11: 'hit'},
    17: {2: 'stand', 3: 'stand', 4: 'stand', 5: 'stand', 6: 'stand', 7: 'stand', 8: 'stand', 9: 'stand', 10: 'stand', 11: 'stand'},
    18: {2: 'stand', 3: 'stand', 4: 'stand', 5: 'stand', 6: 'stand', 7: 'stand', 8: 'stand', 9: 'stand', 10: 'stand', 11: 'stand'},
    19: {2: 'stand', 3: 'stand', 4: 'stand', 5: 'stand', 6: 'stand', 7: 'stand', 8: 'stand', 9: 'stand', 10: 'stand', 11: 'stand'},
    20: {2: 'stand', 3: 'stand', 4: 'stand', 5: 'stand', 6: 'stand', 7: 'stand', 8: 'stand', 9: 'stand', 10: 'stand', 11: 'stand'},
  },
  'soft': {
    13: {2: 'hit', 3: 'hit', 4: 'hit', 5: 'double down', 6: 'double down', 7: 'hit', 8: 'hit', 9: 'hit', 10: 'hit', 11: 'hit'},
    14: {2: 'hit', 3: 'hit', 4: 'hit', 5: 'double down', 6: 'double down', 7: 'hit', 8: 'hit', 9: 'hit', 10: 'hit', 11: 'hit'},
    15: {2: 'hit', 3: 'hit', 4: 'double down', 5: 'double down', 6: 'double down', 7: 'hit', 8: 'hit', 9: 'hit', 10: 'hit', 11: 'hit'},
    16: {2: 'hit', 3: 'hit', 4: 'double down', 5: 'double down', 6: 'double down', 7: 'hit', 8: 'hit', 9: 'hit', 10: 'hit', 11: 'hit'},
    17: {2: 'hit', 3: 'double down', 4: 'double down', 5: 'double down', 6: 'double down', 7: 'hit', 8: 'hit', 9: 'hit', 10: 'hit', 11: 'hit'},
    18: {2: 'stand', 3: 'double down', 4: 'double down', 5: 'double down', 6: 'double down', 7: 'stand', 8: 'stand', 9: 'hit', 10: 'hit', 11: 'hit'},
    19: {2: 'stand', 3: 'stand', 4: 'stand', 5: 'stand', 6: 'stand', 7: 'stand', 8: 'stand', 9: 'stand', 10: 'stand', 11: 'stand'},
    20: {2: 'stand', 3: 'stand', 4: 'stand', 5: 'stand', 6: 'stand', 7: 'stand', 8: 'stand', 9: 'stand', 10: 'stand', 11: 'stand'},
  },
  'pair': {
    2: {2: 'split', 3: 'split', 4: 'split', 5: 'split', 6: 'split', 7: 'split', 8: 'split', 9: 'split', 10: 'split', 11: 'split'},
    4: {2: 'split', 3: 'split', 4: 'split', 5: 'split', 6: 'split', 7: 'split', 8: 'hit', 9: 'hit', 10: 'hit', 11: 'hit'},
    6: {2: 'split', 3: 'split', 4: 'split', 5: 'split', 6: 'split', 7: 'split', 8: 'hit', 9: 'hit', 10: 'hit', 11: 'hit'},
    8: {2: 'hit', 3: 'hit', 4: 'hit', 5: 'split', 6: 'split', 7: 'hit', 8: 'hit', 9: 'hit', 10: 'hit', 11: 'hit'},
    10: {2: 'double down', 3: 'double down', 4: 'double down', 5: 'double down', 6: 'double down', 7: 'double down', 8: 'double down', 9: 'double down', 10: 'hit', 11: 'hit'},
    12: {2: 'split', 3: 'split', 4: 'split', 5: 'split', 6: 'split', 7: 'hit', 8: 'hit', 9: 'hit', 10: 'hit', 11: 'hit'},
    14: {2: 'split', 3: 'split', 4: 'split', 5: 'split', 6: 'split', 7: 'split', 8: 'hit', 9: 'hit', 10: 'hit', 11: 'hit'},
    16: {2: 'split', 3: 'split', 4: 'split', 5: 'split', 6: 'split', 7: 'split', 8: 'split', 9: 'split', 10: 'split', 11: 'split'},
    18: {2: 'split', 3: 'split', 4: 'split', 5: 'split', 6: 'split', 7: 'stand', 8: 'split', 9: 'split', 10: 'stand', 11: 'stand'},
    20: {2: 'stand', 3: 'stand', 4: 'stand', 5: 'stand', 6: 'stand', 7: 'stand', 8: 'stand', 9: 'stand', 10: 'stand', 11: 'stand'},
    22: {2: 'split', 3: 'split', 4: 'split', 5: 'split', 6: 'split', 7: 'split', 8: 'split', 9: 'split', 10: 'split', 11: 'split'},
  }
}

class Hand:
  def __init__(self, cards: list[Card]):
    self.cards = cards

  def add_card(self, card: Card):
    self.cards.append(card)

  def remove_card(self, card: Card):
    self.cards.remove(card)

  def get_sum(self):
    hand_sum = 0
    for card in self.cards:
      # print(f"get_sum: Card: {card}")
      # print(f"get_sum: Summing up value: {card.value}")
      hand_sum += card.value
    return hand_sum
  
  def is_soft(self):
    for card in self.cards:
      if card.value == 11:
        return True
    return False
  
  def drop_ace(self):
    for card in self.cards:
      if card.value == 11:
        card.value = 1
        return True
    return False
  
  def is_pair(self):
    return len(self.cards) == 2 and self.cards[0].value == self.cards[1].value
  
  def calculate_best_action(self, dealer_up_card: Card):
    hand_sum = self.get_sum()
    print(f"Hand Sum: {hand_sum}")
    if hand_sum == 21:
      return 'blackjack'
    elif hand_sum < 5:
      return 'hit'
    elif self.is_pair():
      return decision_table['pair'][hand_sum][dealer_up_card.value]
    elif self.is_soft():
      if hand_sum < 13:
        return 'ERROR: Likely only one ace. Hit'
      # Check for busting with aces, if bust, drop the value of the ace to a 1 and recalculate as a hard hand
      if hand_sum > 21:
        # print("Dropping an ace...")
        self.drop_ace()
        return self.calculate_best_action(dealer_up_card)
        # return decision_table['hard'][hand_sum][int(dealer_up_card.value_string)]
      return decision_table['soft'][hand_sum][dealer_up_card.value]
    elif hand_sum > 21:
      return 'bust'
    elif not self.is_soft():
      return decision_table['hard'][hand_sum][dealer_up_card.value]
    else:
      return 'ERROR'

  def __str__(self) -> str:
    return f"Hand: {self.cards}"