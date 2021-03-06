import deck
import loops

class Player:
    def __init__(self,name):
        self.name = name
        self.hand = []
    def starting_hand(self,decker,defuse):
        self.hand.append(defuse)
        for i in range(4):
            self.hand.append(decker.draw_top())
    def len_hand(self):
        return len(self.hand)
    def print_name(self):
        return(self.name)
    def show_hand(self):
        for i,k in enumerate(self.hand):
            print(str(i)+"-"+k.type)
    def draw(self,decker):
        self.hand.append(decker.draw_top())
    def play_card(self,decker,hand,pick,cards,attack,arr_players,turn_order):
        self.show_hand()
        print("Select a card")
        played_card = loops.choose_loop(self.hand)
        if played_card.cat:
            x = 0
            for i in hand:
                if i.type == played_card.type:
                    x += 1
            if x >= 1:
                if played_card.nope(arr_players,cards,turn_order):
                    hand.remove(played_card)
                    return True,False
                return played_card.steal(hand,self,arr_players,played_card)
            elif x == 0:
                print("You do not have two of those")
                self.hand.append(played_card)
                return True,False
        else:
            if played_card == cards[2]:
                if played_card.nope(arr_players,cards,turn_order):
                    return  True,False
                return played_card.skip(attack,pick)
            elif played_card == cards[3]:
                if played_card.nope(arr_players,cards,turn_order):
                    return True,False
                return played_card.attack(attack,pick)
            elif played_card == cards[4]:
                if played_card.nope(arr_players,cards,turn_order):
                    return True,False
                return played.card.favor(hand,self,arr_players,played_card)
            elif played_card == cards[5]:
                if played_card.nope(arr_players,cards,turn_order):
                    return True,False
                decker.shuffle()
                return True,False
            elif played_card == cards[12]:
                if played_card.nope(arr_players,cards,turn_order):
                    return True,False
                played_card.see_future(decker)
                return pick,attack
            else:
                pick = True
                return pick,attack
