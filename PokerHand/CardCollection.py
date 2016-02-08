# By Taiwo Kareem <taiwo.kareem36@gmail.com>
# Github <https://github.com/tushortz>
# Last updated (08-February-2016)

# Import card class
from Card import Card

# Create card class
class CardCollection:
	# Initialise fields
	def __init__(self):
		self.cards = []

	# Error checks
	def __check__(self, card):
		if not isinstance(card, Card):
			raise ValueError("argument not of type: Card")
		return card

	# String representation
	def __toString__(self, card):
		return "%s%s" % (card.rank, card.suit)

	# Other methods
	def contains(self, card):
		return (self.__check__(card) in self.cards)

	def isEmpty(self):
		return len(self.cards) == 0

	def size(self):
		return len(self.cards)

	def add(self, card):
		if (self.contains(self.__check__(card))):
			raise ValueError("card already present")

		self.cards.append((self.__toString__(card)))

	def sort(self):
		self.cards = sorted(self.cards)