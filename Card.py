import loops

class Card():
    #to make a card you must type Card("Name of Card")
    def check_cat(self,string):
        if "Cat" in string:
            return True
        return False
    def __init__(self,string):
        self.type = string
        self.cat = self.check_cat(self.type)
        # self.image_back = image_back
        # self.image_front = image_front
    def __str__(self):
        return self.type
    #makes another player choose a card to give away to current player
    def favor(self,hand,player,arr_players,played_card):
        card_taken = arr_players[recipient].hand.pop(loops.give_card(arr_players,loops.phase_of_taking(arr_players,player)))
        print(card_taken,"was given")
        recipient.hand.remove(card_taken)
        player.hand.append(card_taken)
        return True,False
    #allows a player to steal a card from another player
    def steal(self,hand,player,arr_players,played_card):
        card_stolen = arr_players[recipient].hand.pop(loops.card_stealing(arr_players,loops.phase_of_taking(arr_players,player)))
        print("You stole",card_stolen.type)
        hand.remove(played_card)
        player.hand.append(card_stolen)
        return True,False
    #makes the player skip a turn
    def skip(self,attack,pick):
        print("Your turn has been skipped")
        pick = False
        return pick,attack
    #the player makes the next person take his turn as well, forcing them to take 2 turns
    def attack(self,attack,pick):
        attack = True
        pick = False
        return pick,attack
    #see future draws the top three cards, prints the three cards, and puts the cards back in the correct positions
    def see_future(self,decker):
        if decker.cards_left() < 3:
            for i in range(decker.cards_left()):
                card = decker.draw_top(i)
                print(card.type)
                decker.add_card(card,i)
        else:
            for i in range(3):
                card = decker.draw_top(i)
                print(card.type)
                decker.add_card(card,i) 