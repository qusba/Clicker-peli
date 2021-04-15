import pygame
class GameLoop():
    def __init__(self,gamelogic,display):
        self.display = display
        self.gamelogic = gamelogic
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", 24)
        self.text = self.font.render("Score: "+str(self.gamelogic.score),True,(255,0,0))
    def start(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit() #pylint: disable = R1722
                    #Pylint ehdotti sys.exitin käyttöä ja sys.exittiä käytettäessä herjasi exitin uudelleenmäärittelystä.
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.gamelogic.click()
            self.text = self.font.render("Score: "+str(self.gamelogic.score),True,(255,0,0))
            self.display.fill((0,0,0))
            self.display.blit(self.text, (10,10))
            pygame.display.flip()
            self.clock.tick(60)
            