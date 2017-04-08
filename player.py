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
    def prompt(self,decker):
        print("Player",self.name)
        pick = True
        while pick:
            choice = input("Do you want to draw a card or play a card from your hand (D/P) : ")
            if choice == "D":
                pick = False
                drawn = decker.draw_top()
                self.hand.append(drawn)
                print("You drew", drawn)
            elif choice == "P":
                pick = False
                self.play_card(self.hand)

    def draw(self,decker):
        self.hand.append(decker.draw_top())
    #def use_card(self,hand):
    #	print(hand,"Select a card you want to pick")
    #	self.play_card()
    def play_card(self,hand):
        self.show_hand()
        print("Select a card")
        is_in = True
        while is_in:
            card_index = int(input("Which card?"))
            if card_index > len(hand) - 1 or card_index < 0 :
                print("Your hand is not that big")
            else:
                played_card = self.hand.pop(card_index)
                is_in = False
        print("You played", played_card)
        #player uses card from hand
