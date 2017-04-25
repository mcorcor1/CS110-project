import pygame

class GUI:
    def __init__(self):

        white = (255,255,255)
        display_width = 1280
        display_height = 720

        self.gameDisplay = pygame.display.set_mode((display_width,display_height))
        pygame.display.set_caption('Exploding Kittens')
        self.gameDisplay.fill(white)
        pygame.display.update()

        cardImg = pygame.image.load("/home/mcorcor1/cs110/finalproject/AofS.png")
        cardImg = pygame.transform.scale(cardImg, (100,100))

        self.middleDeck = pygame.Surface((120,168))
        self.gameDisplay.blit(self.middleDeck, (350,275))
        
        gameExit = False
        
        while not gameExit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True                    
                #print(event) 
            
            pygame.display.update()
        pygame.quit()
        quit()
   
    
    def playerIcon(self, xcor, ycor, numberofPlayers):
        self.xcor = xcor
        self.ycor = ycor
        for i in numberofPlayers:
            self.player = pygame.Surface((100,100))  
            self.gameDisplay.blit(self.player, (xcor,ycor))

    def cardsinHand(self):
        self.card1 = pygame.surface((120,168))
        self.gameDisplay.blit(self.card1, (400,600)) 
                


def main():
    GUI()

main()

