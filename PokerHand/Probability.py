# By Taiwo Kareem <taiwo.kareem36@gmail.com>
# Github <https://github.com/tushortz>
# Last updated (08-February-2016)

# Importing necessary Class
import sys, random
from Deck import Deck
from PokerHand import PokerHand

try:
	import numpy as np
	import matplotlib.pyplot as plt
except ImportError as __err:
	sys.exit("Error: " + str(__err) + "\nInstall with pip install matplotlib\n")

class Probability:
	def __init__(self, rounds=1000, *choices):
		# Variable declarations for counting
		self.flush = 0
		self.fullHouse = 0
		self.threeOfAKind = 0
		self.fourOfAKind = 0
		self.onePair = 0
		self.twoPairs = 0
		self.rounds = rounds
		self.choices = choices

		# Check for empty values
		if len(self.choices) == 0:
			sys.exit("Empty poker type not allowed")

		# Run game 10000 times
		for i in range(self.rounds):
			# Instantiate card and decks
			self.deck = Deck()
			self.deck.shuffle()

			# Play 10 rounds
			for j in range(10):
				self.poker = PokerHand()
				# Pick up 5 cards
				for k in range(5):
					self.poker.add(self.deck.deal())

			# Check if cards are cetain types of pokers
			if self.poker.isFlush():
				self.flush += 1

			elif self.poker.hasFullHouse():
				self.fullHouse += 1

			elif self.poker.hasThreeOfAKind():
				self.threeOfAKind += 1

			elif self.poker.hasFourOfAKind():
				self.fourOfAKind += 1

			elif self.poker.hasOnePair():
				self.onePair += 1

			elif self.poker.hasTwoPairs():
				self.twoPairs += 1


	def show(self):
		# Results
		self.head = "%s hands dealt\n%s\n"
		self.head = self.head % (self.rounds, (len(self.head) - 1) * "=")

		print(self.head)

		for choice in self.choices:
			choice = choice.lower().replace(" ", "")

			if choice == "f" or choice == "flush":
				print("Flush occurred %s times" % self.flush)
				print("Estimated P(Flush) is: %.3f\n" % ((self.flush * 100)/self.rounds))

			elif choice == "fh" or choice == "fullhouse":
				print("Full House occurred %s times" % self.fullHouse)
				print("Estimated P(Full House) is: %.3f\n" % ((self.fullHouse * 100)/self.rounds))

			elif choice == "toak" or choice == "threeofakind":
				print("Three of a kind %s times" % self.threeOfAKind)
				print("Estimated P(Three of a kind) is: %.3f\n" % ((self.threeOfAKind * 100)/self.rounds))

			elif choice == "foak" or choice == "fourofakind":
				print("Four of a kind %s times" % self.fourOfAKind)
				print("Estimated P(Four of a kind) is: %.3f\n" % ((self.fourOfAKind * 100)/self.rounds))

			elif choice == "op" or choice == "onepair":
				print("One Pair %s times" % self.onePair)
				print("Estimated P(One Pair) is: %.3f\n" % ((self.onePair * 100)/self.rounds))

			elif choice == "tp" or choice == "twopairs":
				print("Two Pairs %s times" % self.twoPairs)
				print("Estimated P(Two Pairs) is: %.3f\n" % ((self.twoPairs * 100)/self.rounds))

	def plot(self):
		pokerlists = []
		header = []

		for choice in self.choices:
			choice = choice.lower().replace(" ", "")

			if choice == "f" or choice == "flush":
				pokerlists.append(self.flush)
				header.append("Flush")

			elif choice == "fh" or choice == "fullhouse":
				pokerlists.append(self.fullHouse)
				header.append("Full House")

			elif choice == "toak" or choice == "threeofakind":
				pokerlists.append(self.threeOfAKind)
				header.append("Three of a kind")

			elif choice == "foak" or choice == "fourofakind":
				pokerlists.append(self.fourOfAKind)
				header.append("Four of a kind")

			elif choice == "op" or choice == "onepair":
				pokerlists.append(self.onePair)
				header.append("One Pair")

			elif choice == "tp" or choice == "twopairs":
				pokerlists.append(self.twoPairs)
				header.append("Two Pairs")

		try:
			n_groups = len(pokerlists)
			fig, ax = plt.subplots()
			index = np.arange(n_groups)
			bar_width = 0.5
			opacity = 0.4

			rects1 = plt.bar(index, pokerlists, bar_width,
			                 alpha=opacity,
			                 color='b',
			                 label='Trials: %s' % self.rounds)

			fig.canvas.set_window_title('Poker Hand')
			plt.xlabel('Poker Hands')
			plt.ylabel('Total number of Occurrences')
			plt.title('Poker Hand')
			plt.xticks(index + bar_width, header)
			plt.legend()
			plt.tight_layout()
			plt.show()
		except:
			return "Error: Can't plot graph"