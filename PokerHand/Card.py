# By Taiwo Kareem <taiwo.kareem36@gmail.com>
# Github <https://github.com/tushortz>
# Last updated (08-February-2016)

# Card class
class Card:
	# Initialize necessary field variables
	def __init__(self, *code):
		# Accept two character arguments
		if len(code) == 2:
			rank = code[0]
			suit = code[1]

		# Can also accept one string argument
		elif len(code) == 1:
			if len(code[0]) == 2:
				rank = code[0][0]
				suit = code[0][1]
			else:
				raise ValueError("card codes must be two characters")

		else:
			raise ValueError("card codes must be two characters")

		self.rank = rank
		self.suit = suit

		# All available ranks
		self.RANKS = [
			"A", "2", "3", "4", "5", "6", "7",
			"8", "9", "T", "J", "Q", "K"
		]

		# All available suits
		self.SUITS = ["C", "D", "H", "S"]

		# Error checks
		if not self.rank in self.RANKS:
			raise ValueError("Invalid rank")

		if not self.suit in self.SUITS:
			raise ValueError("Invalid suit")

	# String representation of cards
	def __str__(self):
		return "%s%s" % (self.rank, self.suit)

	# Class Methods
	def getRanks(self):
		return self.RANKS

	def getSuits(self):
		return self.SUITS

	def getRank(self):
		return self.rank

	def getSuit(self):
		return self.suit

	def hashCode(self):
		prime = 31
		result = 1
		result = str(prime * result) + self.rank
		result = str(prime * result) + self.suit

		return result

	def equals(self, thing):
		same = False
		if (thing == self):
			same = True

		elif (thing != None and isinstance(thing, Card)):
			if thing.rank == self.rank and thing.suit == self.suit:
				same = True

		else:
			same = False

		return same

	def compareTo(self, other):
		mySuit = self.SUITS.index(self.suit)
		otherSuit = self.SUITS.index(other.suit)
		difference = mySuit - otherSuit

		if difference == 0:
			myRank = self.RANKS.index(self.rank)
			otherRank = self.RANKS.index(other.rank)
			difference = myRank - otherRank

		return difference