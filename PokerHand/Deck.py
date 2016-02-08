# By Taiwo Kareem <taiwo.kareem36@gmail.com>
# Github <https://github.com/tushortz>
# Last updated (08-February-2016)

# Import needed modules and classes
from CardCollection import CardCollection
from Card import Card
import random

# Create Deck class
class Deck(CardCollection):
	# Initialise necessary class variables
	def __init__(self):
		super(CardCollection, self).__init__()
		self.cards = []
		self.RANKS = [
			"A", "2", "3", "4", "5", "6", "7",
			"8", "9", "T", "J", "Q", "K"
		]
		self.SUITS = ["C", "D", "H", "S"]

		for suit in self.SUITS:
			for rank in self.RANKS:
				self.cards.append((Card(rank, suit)))

	# String representation of class
	def __toString(self, card):
		return "%s%s" % (card.getRank(), card.getSuit())

	# Other class methods
	def deal(self):
		return self.cards.pop(0)

	def shuffle(self):
		self.cards = random.sample(self.cards, len(self.cards))
		return self.cards