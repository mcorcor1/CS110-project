import deck
import player
import Card
#import screen

def initialize():
    exploding_kitten = Card.Card("Exploding Kitten")
    defuse = Card.Card("Defuse")
    skip = Card.Card("Skip")
    attack = Card.Card("Attack")
    rainbow_cat = Card.Card("Rainbow Cat")
    favor = Card.Card("Favor")
    shuffle = Card.Card("Shuffle")
    tacocat = Card.Card("Taco Cat")
    catermelon = Card.Card("Catermelon")
    hairy_potato_cat = Card.Card("Hairy Potato Cat")
    beard_cat = Card.Card("Beard Cat")
    nope = Card.Card("Nope")
    see_future = Card.Card("See the Future")
    decker = deck.Deck()
    arr = []
    arr.append(exploding_kitten)
    arr.append(defuse)
    arr.append(skip)
    arr.append(attack)
    arr.append(favor)
    arr.append(shuffle)
    arr.append(rainbow_cat)
    arr.append(tacocat)
    arr.append(catermelon)
    arr.append(hairy_potato_cat)
    arr.append(beard_cat)
    arr.append(nope)
    arr.append(see_future)
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
        player_name.starting_hand(decker,arr[1])
        arr_players.append(player_name)
    for i in range(num_players-1):
        decker.add_card(exploding_kitten)
    decker.add_card(defuse)
    decker.shuffle()
    return decker,arr_players,arr

def turn_rollover(turn_order,number_players):
    if turn_order == number_players:
        turn_order = 0    
    elif turn_order < 0:
        turn_order = number_players
    return turn_order

def main():
    #screen = screen.make_screen()
    decker,arr_players,cards = initialize()
    for i in range(len(arr_players)):
        print(arr_players[i].print_name())
        arr_players[i].show_hand()
    print(decker.cards_left())
    turn_order = 0
    while len(arr_players) != 1:
        death,attack = arr_players[turn_order].prompt(decker,cards,arr_players)
        if death == True:
            arr_players.pop(turn_order)
            turn_order -= 1
            turn_order = turn_rollover(turn_order,len(arr_players))
        if attack:
            turn_order = turn_rollover(turn_order,len(arr_players))
            turn_order += 1
            death,attack = arr_players[turn_order].prompt(decker,cards,arr_players)
        else:
            turn_order += 1
        turn_order = turn_rollover(turn_order,len(arr_players))

main()