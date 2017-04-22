class Card():
    #to make a card you must type Card("Name of Card")
    def __init__(self,string):
        self.type = string
        # self.image_back = image_back
        # self.image_front = image_front
  #   def __str__(self):
		# return self.type
    def skip(self,attack,pick):
        print("Your turn has been skipped")
        pick = False
        return pick,attack
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