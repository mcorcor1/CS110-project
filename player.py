import deck

class Player:
    def __init__(self,name):
        self.name = name
        self.hand = []
    def starting_hand(self,decker,defuse):
        self.hand.append(defuse)
        for i in range(4):
            self.hand.append(decker.draw_top())
    def print_name(self):
        return(self.name)
    def show_hand(self):
        for card in self.hand:
            print(card)
    def prompt(self,decker,cards,arr_players):
        pick = True
        attack = False
        while pick:
            print("Player",self.name)
            choice = input("Do you want to draw a card or play a card from your hand (D/P) : ")
            if choice == "D":
                pick = False
                drawn = decker.draw_top()
                if drawn == cards[0]:
                    print("EXPLODING KITTEN")
                    death = True
                    for i in range(len(self.hand)):
                        if self.hand[i] == cards[1]:
                            decision = input("Would you like to play your defuse? (y/n)")
                            if decision == "n":
                                print("Why?")
                            elif decision == "y":
                                self.hand.pop(i)
                                self.show_hand()
                                print("You have played a defuse\n There are currently",decker.cards_left(),"cards left in the deck")
                                deck_spot = int(input("Enter the location you want the exploding kitten to be placed"))
                                decker.add_card(cards[0],deck_spot-1)
                                return False,False
                    if death == True:
                        return True,False
                self.hand.append(drawn)
                print("You drew", drawn)
            elif choice == "P":
                pick,attack = self.play_card(decker,self.hand,pick,cards,attack)

    def draw(self,decker):
        self.hand.append(decker.draw_top())
    #def use_card(self,hand):
    #	print(hand,"Select a card you want to pick")
    #	self.play_card()
    def play_card(self,decker,hand,pick,cards,attack):
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
        if played_card == cards[2]:
            print("Your turn has been skipped")
            pick = False
            return pick,attack
        elif played_card == cards[5]:
            decker.shuffle()
            print("The deck has been shuffled")
            pick = True
            return pick,attack
        elif played_card == cards[3]:
            attack = True
            return pick,attack
        else:
            pick = True
            return pick,attack
#player uses card from hand

