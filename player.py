import deck

class Player:
	def __init__(self,name):
		self.name = name
		self.hand = []
	def starting_hand(self,decker):
		self.hand.append(deck.Card("Defuse"))
		for i in range(4):
			self.hand.append(decker.draw_top())
	def print_name(self):
		return(self.name)
	def show_hand(self):
		for card in self.hand:
			print(card)




