import random
class Deck(object):
	def __init__(self):
		self.cards =  ["s1","s2","s3","s4","s5"]
	def deal(self):
		x = self.cards[-1]
		self.cards.pop()
		print "dealing"
		print x
		print len(self.cards)
		return self
	def shuffle(self):
		random.shuffle(self.cards)
		return self

deck = Deck()
deck.shuffle().deal().deal()