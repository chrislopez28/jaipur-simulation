"""Initializes a deck and starting hand"""

import jaipur

deck = jaipur.Deck()
hand = jaipur.Hand()
deck.deal_hand(hand)
print("Created Jaipur deck and hand. Access with 'deck' and 'hand' variables.")
