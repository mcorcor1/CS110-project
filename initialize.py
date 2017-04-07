import deck
import player
#import screen

def initialize():
	exploding_kitten = deck.Card("Exploding Kitten")
	defuse = deck.Card("Defuse")
	skip = deck.Card("Skip")
	attack = deck.Card("Attack")
	rainbow_cat = deck.Card("Rainbow Cat")
	favor = deck.Card("Favor")
	shuffle = deck.Card("Shuffle")
	tacocat = deck.Card("Taco Cat")
	catermelon = deck.Card("Catermelon")
	hairy_potato_cat = deck.Card("Hairy Potato Cat")
	beard_cat = deck.Card("Beard Cat")
	nope = deck.Card("Nope")
	see_future = deck.Card("See the Future")
	decker = deck.Deck()
	for i in range(4):
		decker.add_card(skip)
		decker.add_card(attack)
		decker.add_card(rainbow_cat)
		decker.add_card(favor)
		decker.add_card(shuffle)
		decker.add_card(tacocat)
		decker.add_card(catermelon)
		decker.add_card(hairy_potato_cat)
		decker.add_card(beard_cat)
	for i in range(5):
		decker.add_card(nope)
		decker.add_card(see_future)
	decker.shuffle()
	num_players = -1
	while num_players < 2 or num_players > 5:
		try:
			num_players = int(input("Enter the number of players (2-5): "))
		except ValueError:
			print("That's not a valid integer.")
	arr_players = []
	for i in range(num_players):
		player_name = player.Player(input("Enter the name of player "+str(i+1)+": "))
		player_name.starting_hand(decker)
		arr_players.append(player_name)
	for i in range(num_players-1):
		decker.add_card(exploding_kitten)
	decker.add_card(defuse)
	decker.shuffle()
	return decker,arr_players

def main():
	#screen = screen.make_screen()
	decker,arr_players = initialize()
	for i in range(len(arr_players)):
		print(arr_players[i].print_name())
		arr_players[i].show_hand()
	print(decker.cards_left())
	arr_players[0].prompt(decker)
	# decker.print_deck()
	# print(decker.cards_left())
	# see_future = deck.Card("See the Future")
	# exploding_kitten = deck.Card("Exploding Kitten")
	# skip = deck.Card("Skip")
	# attack = deck.Card("Attack")
	#print(see_future)
	# decker = deck.Deck()
	# decker.add_card(see_future)
	# decker.add_card(exploding_kitten)
	# decker.add_card(skip)
	# decker.add_card(attack)
	# print(decker.draw_top())
	# decker.print_deck()
	#decker.draw_top()
	#decker.draw_bottom()
	# decker.print_deck()
	# print("Space")
	# decker.see_future()
	# print("space")
	# decker.print_deck()
	# decker.print_deck()
	# print("Shuffle")
	# decker.shuffle()
	# decker.print_deck()

	#print(decker)
	#decker.print_deck()

main()
