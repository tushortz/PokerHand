# By Taiwo Kareem <taiwo.kareem36@gmail.com>
# Github <https://github.com/tushortz>
# Last updated (08-February-2016)

# Import necessary class and modules
from CardCollection import CardCollection
from Card import Card

# PokerHand inherits from CardCollection
class PokerHand(CardCollection):
	# Initialzing necessary class variables
	def __init__(self):
		super(CardCollection, self).__init__()
		self.cards = []

	# String representation of class
	def __toString__(self, card):
		return "%s%s" % (card.getRank(), card.getSuit())

	def __str__(self):
		if self.isEmpty():
			return "<empty>"
		else:
			result = ""
			for card in self.cards:
				result += self.__toString__(card) + " "
			return result

	# Invalid input handling
	def __cardCheck(self, score):
		rankCards = []

		if self.size() == 5:
			for card in self.cards:
				rankCards.append(card.getRank())

			rankCards = sorted(rankCards)
			total = 0

			for card in rankCards:
				total += rankCards.count(card)

			if total == score:
				return True
		return False

	# Other class methods
	def add(self, *cardInHand):
		for card in cardInHand:
			self.cards.append(card)

		if len(self.cards) > 5:
			raise ValueError("5 cards already at hand")

	def isFlush(self):
		cardSuits = []
		if len(self.cards) == 5:
			for card in self.cards:
				cardSuits.append(card.getSuit())

			cardSuits = sorted(set(cardSuits))

			if len(cardSuits) == 1:
				return True

		return False


	def hasFourOfAKind(self):
		return self.__cardCheck(17)

	def hasFullHouse(self):
		return self.__cardCheck(13)

	def hasThreeOfAKind(self):
		return self.__cardCheck(11)

	def hasTwoPairs(self):
		return self.__cardCheck(9)

	def hasOnePair(self):
		return self.__cardCheck(7)